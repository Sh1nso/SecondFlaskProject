from flask import Flask, request, render_template
from utils import *

app = Flask(__name__)


@app.route('/')
def main_page():
    """
    Возвращает главную страницу со списком из всех кандидатов
    """
    new_list = []
    for candidate in load_candidates_from_json():
        new_list.append(candidate)
    return render_template('list.html', list_of_candidate=new_list)


@app.route('/candidate/<candidate_id>')
def single_page(candidate_id):
    """
    Возвращает страницу с информацией об одном кандидате по его ID
    """
    return render_template('single.html', candidate=get_candidate(candidate_id))


@app.route('/search/<candidate_name>')
def get_name_page(candidate_name):
    """
    Возвращает станицу со списком кандидатов по имени
    """
    new_list = []
    for candidate in load_candidates_from_json():
        if candidate_name == candidate['name'].split()[0]:
            new_list.append(candidate)
    print(new_list)
    return render_template('search.html', list_of_candidate=new_list, length=len(new_list))


@app.route('/skill/<skill_name>')
def get_skill_page(skill_name):
    """
    Возвращает страницу со списком кандидатов с подходящими навыками
    :param skill_name:
    :return:
    """
    new_list = []
    for candidate in load_candidates_from_json():
        if skill_name.lower() in "".join(candidate["skills"]).lower().split(", "):
            new_list.append(candidate)
    return render_template('skill.html', list_of_candidate=new_list, length=len(new_list), skill=skill_name)


if __name__ == "__main__":
    app.run()

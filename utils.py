from json import loads


def load_candidates_from_json():
    """
    Возвращает список кандидатов
    """
    with open('candidates.json', encoding='utf-8') as file:
        data = loads(file.read())
    return data


def get_candidate(candidate_id):  # не уверен, как делать обозначение, когда возможен возврат разных типов
    """
    Возвращает одного кандидата по его id
    """
    if not candidate_id.isdigit() or int(candidate_id) > len(load_candidates_from_json()):
        return f'У нас нет кандидата с таким id'
    for candidate in load_candidates_from_json():
        if candidate['id'] == int(candidate_id):
            return candidate


def get_candidates_by_name(candidate_name: str) -> dict:
    """
    Возвращает кандидата по имени
    """
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            return candidate


def get_candidates_by_skill(skill_name: str) -> list[dict]:
    """
    Возвращает кандидатов по навыку
    """
    list_of_candidate = []
    for candidate in load_candidates_from_json():
        if skill_name.lower() in "".join(candidate["skills"]).lower().split(", "):
            list_of_candidate.append(candidate)
    return list_of_candidate


print(get_candidates_by_skill('python'))

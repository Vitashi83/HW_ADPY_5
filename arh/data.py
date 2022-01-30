people = [{'name': 'Basta', 'position_id': 1},
          {'name': 'Dobro', 'position_id': 2},
          {'name': 'Splin', 'position_id': 3},
          {'name': 'Link', 'position_id': 2},
          {'name': 'Chaif', 'position_id': 3},
          {'name': 'no name', 'position_id': 1}]

positions = [{'id': 1, 'name': 'repairman', 'salary': 2000},
             {'id': 2, 'name': 'stripper', 'salary': 3000},
             {'id': 3, 'name': 'postman', 'salary': 4000}]


def get_employees():
    return [{'name': p['name'],
             'position': next(i['name'] for i in positions if i['id'] == p['position_id']),
             'id': p['position_id'],
             'salary': next(i['salary'] for i in positions if i['id'] == p['position_id'])} for p in people]
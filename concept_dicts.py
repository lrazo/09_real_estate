lookup = {}

lookup = dict()

lookup = {'age': 42, 'location': 'italy'}

lookup = dict(age=42, location='italy')


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name


gandolf = Wizard('Gandolf', 42)
print(gandolf.__dict__)
print(gandolf.__dict__['level'])
print(gandolf.__dict__['name'])

print(lookup)
print(lookup['location'])

lookup['cat'] = 'Fun code demos'

if 'cat' in lookup:
    print(lookup['cat'])

import collections

User = collections.namedtuple('User', 'id, name, email')
users = [
    User(1, 'user1', 'user1@talkpython.fm'),
    User(2, 'user2', 'user2@talkpython.fm'),
    User(3, 'user3', 'user3@talkpython.fm'),
    User(4, 'user4', 'user4@talkpython.fm'),
    User(5, 'user5', 'user5@talkpython.fm')
]

lookup = dict()

for u in users:
    lookup[u.email] = u

print(lookup['user4@talkpython.fm'])

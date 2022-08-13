class Student(object):
    def __init__(self, id, name, gender, tel):
        self.id = id
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return '%d,%s, %d, %d' % (self.id, self.name, self.gender, self.tel)

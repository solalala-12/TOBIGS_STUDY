class Student:
    def __init__(self, id=None,name=None):
        self.id=id
        self.name=name

    def __str__(self):
        return str(self.id)+" 번 "+self.name

    # 번호순 오름차순
    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, other):
        return self.id == other.id

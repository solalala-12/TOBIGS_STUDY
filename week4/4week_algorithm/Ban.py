class Ban:

    #생성자
    def __init__(self, no=None):
        self.no=no

        #Ban class 안에 student class가 list로 들어간다.
        self.student_list = []


    def __str__(self):
        # Tostring
        return "<"+str(self.no)+"반>"

    #반별 오름차순
    #sort의 기준이 되는 magic method

    def __lt__(self, other):
        return self.no < other.no

    def __eq__(self, other):
        return self.no == other.no
    """
    Student class를 student_list에 append 하는 함수
    def addlist(self,student):
        self.student_list.append(student)
    """

    def count_student(self):
        return len(self.student_list)




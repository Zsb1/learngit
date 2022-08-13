class StudentManager(object):
    def __init__(self):
        self.student_id_list = []
        self.student_name_list = []
        self.student_gender_list = []
        self.phone_number_list = []

    def main(self):
        self.load_student()

        while True:
            self.show_munu()
            a = int(input('请选择您需要的功能序号:'))  # 用户输入功能序号实现调用函数
            if a == 1:
                self.add_student()  # 添加学员
            elif a == 2:
                self.del_student()  # 删除学员
            elif a == 3:
                self.modify_student()  # 修改学员信息
            elif a == 4:
                self.show_student()  # 查询学员信息
            elif a == 5:
                self.all_student()  # 查询所有学员信息
            elif a == 6:
                self.save_student()  # 保存所有学员信息
            elif a == 7:  # 退出系统
                s = input('确定退出吗？\n确认:yes\t否:no\n请输入:')
                if s == 'yes':  # 判断用户时候误操作
                    break
                else:
                    print('请继续操作')

            else:
                print('输入错误,请重新输入')  # 输入的内容不是功能序号则从新输入

    # 静态方法
    @staticmethod
    def show_munu():
        print('请选择下面的功能')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:查询所有学员信息')
        print('6::保存学生信息')
        print('7:退出系统')

    # 添加学生信息
    def add_student(self):

        student_id = int(input('请输入您的学生id:'))
        student_name = input('请输入学生的姓名:')
        student_gender = input('请输入学生的性别:')
        student_tel = int(input('请输入学生的手机号:'))

        if student_id in self.student_id_list:  # 判断用户输入的学生学号是否已经在student_id_list里
            print('学号已存在')
        elif student_name in self.student_name_list:  # 判断用户输入的学生姓名时候已经在student_name_list里
            print('该用户已存在')
        elif student_tel in self.phone_number_list:  # 判断用户输入的学生电话号码是否已经在phone_number_list里
            print('电话号码已存在')
        else:  # 如果都不存在则实现添加功能并打印添加成功
            self.student_id_list.append(student_id)
            self.student_name_list.append(student_name)
            self.student_gender_list.append(student_gender)
            self.phone_number_list.append(student_tel)
            print('添加成功')

        print(self.student_id_list)
        print(self.student_name_list)
        print(self.student_gender_list)
        print(self.phone_number_list)

    # 删除学生信息
    def del_student(self):
        delete_name = input('请输入要删除的学生姓名:')

        delete_name_index = self.student_name_list.index(delete_name)

        if delete_name not in self.student_name_list:  # 判断学生是否在student_name_list列表里
            print('学生不存在')
        else:  # 进一步确认用户是否删除
            d = input('您确定要删除此学员的所有信息吗?\n确认:yes  否:no\n请输入:')
            if d == 'yes':  # 输入yes则进行删除功能
                self.student_name_list.remove(delete_name)
                del self.student_id_list[delete_name_index]
                del self.student_gender_list[delete_name_index]
                del self.phone_number_list[delete_name_index]
            else:  # 输入no则退出
                print('退出')

        print(self.student_id_list)
        print(self.student_name_list)
        print(self.student_gender_list)
        print(self.phone_number_list)

    # 修改学生信息
    def modify_student(self):
        modify_name = input('请输入要修改的学生姓名:')

        modify_name_index = self.student_name_list.index(modify_name)  # 通过学生姓名获取其下标

        if modify_name not in self.student_name_list:  # 判断学生是否在student_name_list列表里
            print('找不到此学员')
        else:
            print('1:修改学员学号')
            print('2:修改学员姓名')
            print('3:修改学员电话号码')
            print('4:修改学生性别')
            print('例:如果要修改学号和电话号码则输入12')
            b = int(input('请输入您要修改功能的序号:'))  # 用户输入序号实现修改功能
            if b == 1:
                after_id = int(input('请输入修改后的学号:'))
                self.student_id_list[modify_name_index] = after_id
            elif b == 2:
                after_name = input('请输入修改后的姓名:')
                self.student_name_list[modify_name_index] = after_name
            elif b == 3:
                after_phone = int(input('请输入修改后的电话号码:'))
                self.phone_number_list[modify_name_index] = after_phone
            elif b == 4:
                after_gender = input('请输入修改后的学生性别:')
                self.student_gender_list[modify_name_index] = after_gender
            elif b == 12:
                after_id = int(input('请输入修改后的学号:'))
                after_name = input('请输入修改后的姓名:')
                self.student_id_list[modify_name_index] = after_id
                self.student_name_list[modify_name_index] = after_name
            elif b == 13:
                after_id = int(input('请输入修改后的学号:'))
                after_phone = int(input('请输入修改后的电话号码:'))
                self.student_id_list[modify_name_index] = after_id
                self.phone_number_list[modify_name_index] = after_phone
            elif b == 14:
                after_id = int(input('请输入修改后的学号:'))
                after_gender = input('请输入修改后的学生性别:')
                self.student_id_list[modify_name_index] = after_id
                self.student_gender_list[modify_name_index] = after_gender
            elif b == 23:
                after_name = input('请输入修改后的姓名:')
                after_phone = int(input('请输入修改后的电话号码:'))
                self.student_name_list[modify_name_index] = after_name
                self.phone_number_list[modify_name_index] = after_phone
            elif b == 24:
                after_name = input('请输入修改后的姓名:')
                after_gender = input('请输入修改后的学生性别:')
                self.student_name_list[modify_name_index] = after_name
                self.student_gender_list[modify_name_index] = after_gender
            elif b == 123:
                after_id = int(input('请输入修改后的学号:'))
                after_name = input('请输入修改后的姓名:')
                after_phone = int(input('请输入修改后的电话号码:'))
                self.student_id_list[modify_name_index] = after_id
                self.student_name_list[modify_name_index] = after_name
                self.phone_number_list[modify_name_index] = after_phone
            elif b == 134:
                after_id = int(input('请输入修改后的学号:'))
                after_name = input('请输入修改后的姓名:')
                after_gender = input('请输入修改后的学生性别:')
                self.student_id_list[modify_name_index] = after_id
                self.student_name_list[modify_name_index] = after_name
                self.student_gender_list[modify_name_index] = after_gender
            elif b == 234:
                after_name = input('请输入修改后的姓名:')
                after_phone = int(input('请输入修改后的电话号码:'))
                after_gender = input('请输入修改后的学生性别:')
                self.student_name_list[modify_name_index] = after_name
                self.phone_number_list[modify_name_index] = after_phone
                self.student_gender_list[modify_name_index] = after_gender

        print(self.student_id_list)
        print(self.student_name_list)
        print(self.student_gender_list)
        print(self.phone_number_list)

    # 查询学生信息
    def show_student(self):

        query_name = input('请输入您要查询的学生的姓名:')  # 用户输入需要查询的学生姓名

        if query_name not in self.student_name_list:
            print('这名学生不存在')
        query_name_index = self.student_name_list.index(query_name)  # 通过学生星星获取其下标

        # 打印student_id_list、student_gender_list、student_name_list、phone_number_list列表内容
        print('学号:%d' % self.student_id_list[query_name_index])
        print('姓名:%s' % self.student_name_list[query_name_index])
        print('性别:%s' % self.student_gender_list[query_name_index])
        print('电话号码:%d' % self.phone_number_list[query_name_index])

    # 查询所有学生信息
    def all_student(self):
        for all_student_id, all_student_name, all_student_gender, all_phone_number in zip(self.student_id_list,
                                                                                          self.student_name_list,
                                                                                          self.student_gender_list,
                                                                                          self.phone_number_list, ):
            print(
                '学号:%d\n姓名:%s\n性别:%s\n电话号码:%d' % (
                    all_student_id, all_student_name, all_student_gender, all_phone_number))

    # 保存学生信息
    def save_student(self):
        f = open('student.data', 'w')

        a = [self.student_id_list, self.student_name_list, self.student_gender_list, self.phone_number_list]
        f.write(str(a))

        f.close()

        print('保存成功')

    # 加载学生信息
    def load_student(self):
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = eval(f.read())
            self.student_id_list, self.student_name_list, self.student_gender_list, self.phone_number_list = data
        finally:
            f.close()

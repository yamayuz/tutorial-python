
class UserInfo:
    def __init__(self, name, birth, address):
        self.name = name
        self.birth = birth
        self.address = address


class TestPrivate:
    def __init__(self):
        self.var1 = 'var1'
        self.__var2 = 'var2'

    def method1(self):
        print('method1')

    def __method2(self):
        print('method2')

    def method3(self):
        print(self.var1)
        print(self.__var2)
        self.method1()
        self.__method2()




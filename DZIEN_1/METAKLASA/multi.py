class MultiBases(type):
    def __new__(cls,clsname,bases,attrs):
        if len(bases) > 1:
            raise TypeError("w tych klasach może tylko jednodziedziczyć!!!")
        return super().__new__(cls,clsname,bases,attrs)

class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B(Base):
    pass

class C(A,B):
    pass


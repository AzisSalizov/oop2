

class Matreshka:
   def __init__(self , body_color , eyes_color , name ):
      self.body_color = body_color
      self.eyes_color = eyes_color
      self.name = name
      
   def __new__(cls, *args , **kwargs ):
      print(f'запуск __new__ {cls}')
      return super().__new__(cls)
   
   def seyHello (self) :
      print(f'Привет матрешка имя {self.name}')
   
A = Matreshka('red' , 'blue' , 'Amina')
# A.seyHello()

# print(f'Тело : {A.body_color} \nГлаза : {A.eyes_color} \nИмя : {A.name}')



class Car :
   def __init__(self , name , release  , car_color) :
      self.name = name 
      self.release = release 
      self.car_color = car_color 


class ToyotaCamry(Car) :
   def __init__(self, name, release, car_color , moduly):
      super().__init__(name, release, car_color)
      self.moduly = moduly

class SUV(Car) :
   def __init__(self, name, release, car_color ):
      super().__init__(name, release, car_color)
   
car = Car('Мерс' , 2019 , 'Черный')
car2 = ToyotaCamry('Toyota Camry' , 2017 , 'Белый' , 'Hoco')
car3 = SUV('Внедорожник' , 2014 , 'Черный')
print(f' Марка : {car.name} \n Выпуск : {car.release} \n Цвет : {car.car_color} ')
print('---' *50)
print(f' Марка : {car2.name} \n Выпуск : {car2.release} \n Цвет : {car2.car_color}')
print('---' *50)
print(f' Марка : {car3.name} \n Выпуск : {car3.release} \n Цвет : {car3.car_color}')


   
class Employee :
   def __init__(self , name , surname  , gender , directions) :
      self.name = name 
      self.surname = surname 
      self.gender = gender 
      self.directions = directions 


class Python(Employee) :
   def __init__(self, name, surname, gender , directions):
      super().__init__(name, surname, gender , directions)

class Js(Employee) :
   def __init__(self, name, surname, gender , directions ):
      super().__init__(name, surname, gender ,directions)
   
empl = Employee('Раха' , 'Akim' , 'мужской' , 'Teamlead')
empl2 = Python('Кама' , 'Kamalov' , 'Мужской' , 'Python')
empl3 = Js('Катя' , 'Катюхина' , 'Женский' , 'Js')
print(f' Имя : {empl.name} \n фамилия : {empl.surname} \n пол : {empl.gender} \n направления : {empl.directions} ')
print('---' *50)
print(f' имя : {empl2.name} \n фамилия : {empl2.surname} \n пол : {empl2.gender} \n направления : {empl2.directions}')
print('---' *50)
print(f' имя : {empl3.name} \n фамилия : {empl3.surname} \n пол : {empl3.gender} \n направления : {empl3.directions}')



class Human :
   
   def __init__(self , name , age , favorite_lesson):
      self.name = name
      self.age = age
      self.favorite_lesson = favorite_lesson
   
   def __str__(self) :
      return f'{self.name} , {self.age} , {self.favorite_lesson}'
class Teacher(Human) :
   
   def __init__(self, name, age , favorite_lesson ,  specialy , salary ):
      self.specialy = specialy
      self.salary = salary
      super().__init__(name, age , favorite_lesson) 
      
   def __str__(self):
      return f'{self.name} , {self.age} , {self.specialy} , {self.favorite_lesson} , {self.salary}'

class Student(Human) :
   
   def __init__(self, name, age, favorite_lesson , grade):
      self.grade = grade
      super().__init__(name, age, favorite_lesson )
      
   def __str__(self):
      return f'{self.name} , {self.age} , {self.specialy} , {self.favorite_lesson} , {self.grade}'
   
human = Human('ALik' , 19 , 'IT')
teacher = Teacher('Malik' , 22 , 'Programmer' , 'Math' , 15000 )
student = Teacher('anvar' , 14 , 'student' , 'Math' , 5  )
print(human)
print(teacher)
print(student)
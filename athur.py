class person:
  def __init__(self,name,age,height):
      self.name = name
      self.age = age
      self.height = height
      
  def greetings(name):
      print ("Hello %s",name)
  
  def getHeight():
      print(self.height)
      
  
athur = person()
athur.greetings("Patrick")
athur.getHeight()
      

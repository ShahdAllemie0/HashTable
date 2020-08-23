class HashTable:
  
  def __init__(self,array_size):
    self.array_size=array_size
    self.dict={"A":[],"B":[],"C":[],"D":[]}


  def hash_c(self,score):  
    if score>= 90:
         return "A"
    elif score>= 80:
         return "B"
    elif score>= 70:
          return "C"
    elif score>= 60:
          return "D"
    else:
          return None
         

  def insert(self,name,score): 

    c=self.hash_c(score)

    if c is not None:
      current_value=self.dict[c]
      if (len(current_value))<self.array_size:
           current_value.append({"Name":name,"Score":score})
          

  def printData(self):
    for f in self.dict:
        print(f'class:{f} Name: {f["name"]} Score: {f["score"]}')




size=int(input("Enter maximum number of students in class: "))
s=HashTable(size)
students = [
    {
        "name": "Jean-Luc Garza",
        "score": 24
    },
    {
        "name": "Teddy Munoz",
        "score": 79
    },
    {
        "name": "Georgia Ali",
        "score": 17
    },
    {
        "name": "Vicky Calhoun",
        "score": 8
    },
    {
        "name": "Awais Weaver",
        "score": 65
    },
    {
        "name": "Athena Kline",
        "score": 52
    },
    {
        "name": "Zacharia Whitaker",
        "score": 38
    },
        {
        "name": "Clarice Davenport",
        "score": 99
    },
    {
        "name": "Viktoria Flynn",
        "score": 84
    },
    {
        "name": "Ianis Crossley",
        "score": 20
    },
    {
        "name": "Johnnie Owens",
        "score": 74
    },
    {
        "name": "Emily-Rose Erickson",
        "score": 33
    },
    {
        "name": "Adeel Nieves",
        "score": 100
    },
    {
        "name": "Dustin Villegas",
        "score": 98 
    },
    {
        "name": "Maxine Hughes",
        "score": 65
    },
    {
        "name": "Bilaal Harding",
        "score": 79
    },
    {
        "name": "Maddie Ventura",
        "score": 71
    },
    {
        "name": "Leroy Rees",
        "score": 44
    },
    {
        "name": "Wanda Frank",
        "score": 73
    },
    {
        "name": "Margaux Herbert",
        "score": 80
    },
    {
        "name": "Ali Rios",
        "score": 70
    },
    {
        "name": "Nigel Santiago",
        "score": 25
    },
    {
        "name": "Markus Greene",
        "score": 78
    },
    {
        "name": "Harlan Parrish",
        "score": 97
    },
    {
        "name": "Baran Davidson",
        "score": 43
    },
    {
        "name": "Seth Rodriguezh",
        "score": 67
    },
    {
        "name": "Diego Mayer",
        "score": 100
    }
]



for x in students:
    s.insert(x["name"],x["score"])


print(s.dict)


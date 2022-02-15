# make a program that calculates your final grade in a class based on overall points
# first draft

class Calculation:
    
    def __init__(self, range1, v1, v2, v3, v4):
        self.range1 = range1
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        
    def calc_percentage(self):
        grade = (self.v1/self.v2)*100
        return grade

            
        

ticker = 0
counter = '*'
names_and_points = {}
random = int(input("How many inputs to you have??"))
loop_range = random*counter

for i in range(len(loop_range)):
    name = input('What is the category you want to calculate?')
    points = float(input(f'Input total points of: {name}: '))
    names_and_points[name] = points 

total_points = sum(names_and_points.values())
user_points = []
for i in names_and_points.keys():
    user_attained = float(input(f'What points have you attained on {i}: '))
    user_points.append(user_attained)
total_attained_points = sum(user_points)

final = Calculation(0, total_attained_points, total_points, 0, 0)
final_grade = final.calc_percentage()
print(final_grade)



class Calculation:
    
    def __init__(self, range1, v1, v2, v3, v4):
        self.range1 = range1
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        
    def calc_percentage(self):
        grade = (self.v1/self.v2)*100
        final_grade = round(grade, 2)
        return final_grade

# ----------------------------------------------

ticker = 0
counter = '*'
names_and_points = {}
print('We will split up each point structure into "categories".\nSuch as exams, hw, final, etc.')
random = int(input("How many categories do you want to calculate?\nInput a number: "))
loop_range = random*counter
user_points = []
for i in range(len(loop_range)):
    ticker += 1
    name = input(f'Please input the name of category {ticker}: ')
    points = float(input(f'Input total points possible of {name}: '))
    user_attained = float(input(f'How many points have you attained on {name}: '))
    names_and_points[name] = points 
    user_points.append(user_attained)

total_points = sum(names_and_points.values())
total_attained_points = sum(user_points)

final = Calculation(0, total_attained_points, total_points, 0, 0)
final_grade = final.calc_percentage()
print(f'Your current/final grade is: {final_grade}')

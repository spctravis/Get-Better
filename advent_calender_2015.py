"""
https://adventofcode.com/2015
"""
#Day 1
"""
puzzle_input="C:\\Users\\dukes\\Documents\\AdventCal\\1puzzle.txt"
puzzle=open(puzzle_input, "r")
puzzle_input=puzzle.readline()

floors_up=puzzle_input.count("(")
floors_down=puzzle_input.count(")")
total_floors=floors_up - floors_down
puzzle.close()
print(total_floors)

#part 2
count=0
floor=0
for i in puzzle_input:
    count=count+1
    if i == "(":
        floor=floor+1
    elif i == ")":
        floor=floor-1
    if floor==-1:
        break

print(count)
"""
#Day 2

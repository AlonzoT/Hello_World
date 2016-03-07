#Compute the Area and Circumference of a function


# declare variables and constants
PI = 3.14

#function definition

def area_circum(radius):
    area = PI*radius**2
    circum= 2*PI*radius**2
    return area, circum

#main() function

def main():
    my_area = 0.0
    my_circum = 0.0
    #get the radius from the user
    radius = float(input('enter the radius of the circle '))

    my_area, my_circum = area_circum(radius)
    print ('The area is ',my_area, ' and the circumference is  ',my_circum)


main()


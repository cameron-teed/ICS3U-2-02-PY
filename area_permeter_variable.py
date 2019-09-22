#!usr/bin/env python
# Created by: Cameron Teed
# Created On: September 2019
# This program calculates the area and perimeter of a circle with the
#   radius of 20mm


def main():
    # This function calculates the area and permeter

    # Input
    lenght = int(input("enter length of the rectangle (mm): "))
    width = int(input("enter the width of the rectangle (mm): "))

    # Procces
    area = lenght*width
    permeter = 2*(lenght+width)

    # Output
    print("")
    print("area is {} mm**2".format(area))
    print("permeter is {} mm".format(permeter))


if __name__ == "__main__":
    main()

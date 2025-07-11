year = int(input("Year: " ))
if 1 <= year <= 9999:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f"12/09/{year:04}")
    else:
        print(f"13/09/{year:04}")
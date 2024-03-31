def find_average(numbers):
    sum_numbers = sum(numbers)
    length_numbers = len(numbers)

    if length_numbers == 0:
        return 0
    
    average = sum_numbers/length_numbers
    print(average)

array = [2,3,5,6,4,2,6]
find_average(array)

def find_average(arrray):
    try:
        return sum(array)/len(array)
    except ZeroDivisionError:
        return 0
    

array = [2,3,5,6,4,2,6]
find_average(array)

def abbrev_name(name):
    # Split the name into two words based on whitespace
        first_name, last_name = name.split(" ")

    # Get the first character of each word and convert to uppercase
        initials = first_name[0].upper() + "." + last_name[0].upper()

        return initials

name = abbrev_name("Bunamin Adams")
print(name)


 
for ( i = 1; i < 3; i++){
     print(i)
}
print("Go!")
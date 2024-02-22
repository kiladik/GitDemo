# add 5 different numbers to a list and print the sum of the numbers
# add 5 different numbers to a list and print the average of the numbers        
    
def main():
    # add 5 different numbers to a list and print the sum of the numbers
    numbers = [1, 2, 3, 4, 5]
    sum = 0
    for number in numbers:
        sum += number
    print("The sum of the numbers is", sum)
    
    # add 5 different numbers to a list and print the average of the numbers
    average = sum / len(numbers)
    print("The average of the numbers is", average)

# Problem 1: Odd/Even Number
def odd_even(n):
    """
    Checks if a number is even or odd.

    Parameters
    ----------
    n : int
        Number to check for even or odd.

    Returns
    -------
    bool
        True if n is even, False if n is odd.
    """
    if n % 2 == 0:
        # Return True if n is divisible by 2 (even)
        return True
    else:
        # Return False if n is not divisible by 2 (odd)
        return False
    
# Problem 2: Prime Number
def prime_number(n):
    """
    Checks if a number is prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Parameters
    ----------
    n : int
        Number to check for primality.

    Returns
    -------
    bool
        True if n is prime, False if not.
    """
    # Handle numbers less than or equal to 1 (not prime)
    if n <= 1:
        return False
    
    # Special case for 2 (the only even prime)
    elif n == 2:
        return True

    # Check divisibility by numbers from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by i, it's not prime
        if n % i == 0:
            return False
    
    # If no divisors found up to the square root, n is prime
    return True

# Problem 3: Leap Year
def is_leap(y):
    """
    Checks if a year is a leap year.

    Leap years are divisible by 4 except for end-of-century years which must be divisible by 400. This means that the year 2000 was a leap year, but the year 1900 was not.

    Parameters
    ----------
    y : int
        Year to check for leap year status.

    Returns
    -------
    bool
        True if y is a leap year, False if not.
    """
    # Condition 1: Divisible by 4 but not 100
    cond1 = y % 4 == 0 and y % 100 != 0
    # Condition 2: Divisible by 400
    cond2 = y % 400 == 0

    # If either condition is true, it's a leap year
    if (cond1 or cond2):
        return True
    # Else not a leap year
    else:
        return False

# Problem 4: Armstrong Number
def armstrong_number(num):

    """
    Checks if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

    Parameters
    ----------
    num : int
        Number to check for Armstrong number status.

    Returns
    -------
    bool
        True if num is an Armstrong number, False if not.
    """
    # Count the number of digits
    dig_count = 0
    temp = num
    while temp != 0:
        dig_count += 1
        temp = temp // 10
    
    # Calculate the sum of digits raised to the power of dig_count
    temp = num
    arm_num = 0
    while temp != 0:
        dig = temp % 10
        arm_num += dig ** dig_count
        temp = temp // 10
    
    # Check if the sum is equal to the original number
    return arm_num == num

# Problem 5: Fibonacci Series
def fibo_seq(n):
    """
    Generates the Fibonacci sequence up to the nth term.

    Parameters
    ----------
    n : int
        The number of terms in the Fibonacci sequence to generate.

    Returns
    -------
    list
        A list of the first n terms of the Fibonacci sequence, starting with 0 and 1.
    """
    # Initialize the first term to 0
    f_term = 0
    # Initialize the second term to 1
    s_term = 1
    # Create a list to store the sequence
    res_arr = [f_term, s_term]
    
    # Handle cases where n is less than or equal to 2
    if n <= 2:
        return res_arr
    
    # Generate the remaining terms using a while loop
    while n > 0:
        # Calculate the next term
        n_term = f_term + s_term
        # Append the next term to the list
        res_arr.append(n_term)
        # Update the first and second terms
        f_term, s_term = s_term, n_term
        # Decrement the counter
        n -= 1
    
    return res_arr

# Problem 6: Identify Palimdrome
def is_palimdrome(ele):
    """
    Checks if a given number or string is a palindrome.

    Parameters
    ----------
    ele : int or str
        The number or string to check.

    Returns
    -------
    bool
        True if the given element is a palindrome, False otherwise.
    """
    # Check if the element is an integer
    if type(ele) == int:
        temp = ele
        rev_num = 0
        
        # Continue the loop until all digits have been processed
        while temp != 0:
            # Extract the last digit of temp
            dig = temp % 10
            # Append the extracted digit to the reversed number
            rev_num = rev_num * 10 + dig
            # Remove the last digit from temp
            temp = temp // 10
        
        # Compare the original and reversed numbers
        return rev_num == ele
    
    # Check if the element is a string
    elif type(ele) == str:
        # Initialize an empty string to store the reversed characters
        rev_str = ""
        
        # Iterate over the characters in reverse order
        for i in range(len(ele)-1, -1, -1):
            # Append the current character to the reversed string
            rev_str += ele[i]
        
        # Compare the original and reversed strings
        return rev_str == ele

# Problem 7: Print star pattern
def pyramid_print(patternType, height):
    """
    Prints a pyramid pattern based on the given type and height.

    Parameters
    ----------
    patternType : str
        The type of pyramid pattern to print. Can be either "pyramid" or "diamond".
    height : int
        The height of the pyramid pattern.

    """
    def erect_pyramid(height):
        # Outer loop for rows
        for i in range(height):
            # Print spaces before stars
            for j in range(height - i - 1):
                print(" ", end="")
            # Print stars
            for j in range(2 * i + 1):
                print("*", end="")
            # Print spaces after stars
            for j in range(height - i - 1):
                print(" ", end="")
            print()  # Move to the next line
            
    def inverted_pyramid(height):
        # Outer loop for rows
        for i in range(height):
            # Print spaces before stars
            for j in range(i):
                print(" ", end="")
            # Print stars
            for j in range(2 * height - (2 * i + 1)):
                print("*", end="")
            # Print spaces after stars
            for j in range(i):
                print(" ", end="")
            print()  # Move to the next line

    if patternType == "pyramid":
        erect_pyramid(height)
    
    elif patternType == "diamond":
        erect_pyramid(height)
        inverted_pyramid(height)

# Problem 8: Find factorial
def factorial(num):
    """
    This function calculates the factorial of a given number.
    
    Parameters:
    num (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of num.
    
    Edge cases:
    - If num is negative, it returns None.
    - If num is zero, it returns 1.
    """
    if num < 0:
        return None
    
    if num == 0:
        return 1
    
    # Initialize factorial to 1
    fact = 1
    # Loop until num becomes 0
    while num != 0:
        # Multiply factorial by num
        fact *= num
        # Decrement num
        num = num - 1
    
    return fact

# Problem 9: Summing Digits of a number
def digit_sum(num):
    """
    This function calculates the sum of digits of a given number.
    
    Parameters:
    num (int): The number to calculate the sum of digits of.
    
    Returns:
    int: The sum of the digits of num.
    """

    # Initialize the sum to 0
    dig_sum = 0

    # Loop until all digits are processed
    while num != 0:
        # Extract the last digit
        dig = num % 10
        # Add the digit to the sum
        dig_sum += dig
        # Remove the last digit from the number
        num = num // 10
    
    # Return the calculated sum
    return dig_sum

# Problem 10: GCD
def find_gcd(a, b):
    """
    This function finds the greatest common divisor (gcd) of two numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    # Initialize the GCD to 1
    gcd = 1
    # Iterate from 1 to the minimum of a and b
    for i in range(1, min(a, b) + 1):
        # Check if i divides both a and b
        if a % i == 0 and b % i == 0:
            # Update the GCD if i is a common divisor
            gcd = i
    
    return gcd

# Problem 11: LCM
def find_lcm(a, b):
    """
    This function finds the least common multiple (lcm) of two numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The least common multiple of a and b.
    """
    # Find the greater of a and b
    greater = max(a, b)
    # Find the smaller of a and b
    smallest = min(a, b)
    # Iterate from the greater number to the product of a and b, incrementing by the greater number    
    for i in range(greater, a*b+1, greater):
        # Check if i is divisible by the smaller number    
        if i % smallest == 0:
            return i

# Problem 12: Count vowels and consonants
def find_vowel_consonant(str):
    # Remove spaces from the string
    """
    This function takes a string and counts the number of vowels and consonants present in the string.
    
    Parameters:
    str (str): The string to be analyzed.
    
    Returns:
    None
    """
    filtered_str = str.replace(" ", "")
    
    vowels = "aeiouAEIOU"
    vowel_count = 0
    cons_count = 0

    for char in filtered_str:
        # Check if the character is a vowels string and increment the vowel count
        if char in vowels:
            vowel_count += 1
        # else increment the consonant count
        else:
            cons_count += 1
    
    print( f"Vowels: {vowel_count}, Consonants: {cons_count}")

# Problem 13: Reverse the string
def reverse_string(str):
    """
    This function takes a string and returns the reversed string.
    
    Parameters:
    str (str): The string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    rev_str = ""
    
    # Iterating through string from last index to first index
    for i in range(len(str) - 1, -1, -1):
        # Concatenating the character to rev_str variable
        rev_str += str[i]
    
    return rev_str

# Problem 14: Finding the Largest and Smallest Numbers in an Array
def find_largest_and_smallest(arr):
    """
    This function takes an array of numbers and finds the largest and smallest element in it.
    
    Parameters:
    arr (list): The list of numbers to be searched.
    
    Returns:
    None
    """
    # Assign largest as negative infinity so when we use it to compare with
    # array element it will be smallest and store the largest element of array
    largest = float("-inf")
    # By the same logic assign the smallest variable as infinity
    smallest = float("inf")

    # Iterate through the array
    for i in range(len(arr)):
        # Compare largest and current array element using max function
        largest = max(largest, arr[i])
        # Compare smallest and current array element using min function
        smallest = min(smallest, arr[i])

    print( f"Largest: {largest}, Smallest: {smallest}")

# Problem 15: Sorting an Array
def sort_array(arr):
    # Bubble sort algorithm 
    """
    This function takes an array of numbers and sorts it in ascending order using bubble sort algorithm.
    
    Parameters:
    arr (list): The list of numbers to be sorted.
    
    Returns:
    None
    """
    for i in range(len(arr)):
        for i in range(len(arr) - i - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    
    print(arr)

# Problem 16: Finding the Sum of Elements in an Array
def sum_of_arr(arr):
    """
    This function takes an array of numbers and adds up all the elements of array.
    
    Parameters:
    arr (list): The list of numbers to be summed.
    
    Returns:
    None
    """
    arr_sum = 0
    
    # Iterate through the array to add up the elements of array in arr_sum
    # variable
    for i in range(len(arr)):
        arr_sum += arr[i]
    
    print(arr_sum)

# Problem 17: Checking for Armstrong Numbers in a Range
def check_for_armstrong_numbers(range_arr):
    """
    This function takes an array with two elements which represent the upper bound and lower bound of a range and prints out all the armstrong numbers in the range.

    Parameters:
    range_arr (list): The list of two elements which represent the range.

    Returns:
    None
    """
    # Extracting upper bound and lower bound of the range
    start = range_arr[0]
    end = range_arr[1]
    
    res_arr = []
    
    # Function for checking if a number is armstrong or not:
    def armstrong_number(num):
            # Edge case for detecting the single digit numbers greater than one
            if 1 < num < 10:
                return False

            if num == 1:
                return True
            
            # Count the number of digits
            dig_count = 0
            temp = num
            while temp != 0:
                dig_count += 1
                temp = temp // 10
            
            # Calculate the sum of digits raised to the power of dig_count
            temp = num
            arm_num = 0
            while temp != 0:
                dig = temp % 10
                arm_num += dig ** dig_count
                temp = temp // 10
            
            # Check if the sum is equal to the original number
            return arm_num == num

    # Iterate through the range and check if the number is armstrong or not!
    for i in range(start, end + 1):
        if armstrong_number(i):
            res_arr.append(i)
    
    print(res_arr)

# Problem 18: Generating multiplication tables
def multiplication_table(num):
    """
    Prints the multiplication table for the given number up to 10.

    Parameters:
    num (int): The number for which the multiplication table is to be printed.

    Returns:
    None
    """
    for i in range(1, 11):
        product = num * i
        print(f"{num} X {i} = {product}")

# Problem 19: Finding Prime Numbers in a Range
def prime_number_range(range_arr):

    
    # Extracting upper bound and lower bound of the range    
    start = range_arr[0]
    end = range_arr[1]

    res_arr = []
    
    def prime_number(n):
        # Handle numbers less than or equal to 1 (not prime)
        if n <= 1:
            return False
        
        # Special case for 2 (the only even prime)
        elif n == 2:
            return True

        # Check divisibility by numbers from 2 to the square root of n
        for i in range(2, int(n**0.5) + 1):
            # If n is divisible by i, it's not prime
            if n % i == 0:
                return False
        
        # If no divisors found up to the square root, n is prime
        return True


    # Iterate through the range and check if the number is prime or not!
    for i in range(start, end + 1):
        if prime_number(i):
            res_arr.append(i)
    
    print(res_arr)

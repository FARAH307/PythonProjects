
# Authors: TODO: Abdullahi Farah

# I have created a brute force method for getting the composite numbers of any number which contains threee functions 


def num_divisors(n):
    """Given an integer input n, return the number of positive integers that are
    divisors of n
    (including 1 and itself)"""
    count = 0

    # this checks if n is 0 or negative number it will return 0
    if n <=0:
        return 0
    
    # this for loop will check every that is divisible by i and then count it which then gets returned the count 
    
    for i in range(1,n+1):
        if n % i == 0:
            count = count + 1
    return count 









def is_highly_composite_number(n):
    """ an integer n is a highly composite number if and only if it is a positive
    integer with
    more divisors than any positive interger smaller than it."""

    if n <= 0:
        return 0 
    for i in range(1, n+1):
        if num_divisors(i) >= num_divisors(n):
            return False 
    return True 

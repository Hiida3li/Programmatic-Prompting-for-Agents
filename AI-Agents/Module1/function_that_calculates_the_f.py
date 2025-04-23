
def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    The factorial of a non-negative integer n, denoted as n!, is the product 
    of all positive integers less than or equal to n. The factorial of 0 is 
    defined as 1.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer n.

    Raises:
    ValueError: If n is a negative integer, since factorial is undefined for negative numbers.

    Examples:
    ---------
    >>> factorial(5)
    120
    # Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120
    
    >>> factorial(0)
    1
    # Explanation: By definition, 0! = 1

    >>> factorial(1)
    1
    # Explanation: 1! = 1

    >>> factorial(3)
    6
    # Explanation: 3! = 3 * 2 * 1 = 6
    
    Edge Cases:
    ----------
    1. If n is 0, the output should be 1, as 0! = 1 by definition.
    2. If n is negative, a ValueError is raised, since the factorial is not defined for negative integers.

    Notes:
    ------
    - This implementation uses a recursive approach to calculate the factorial.
    - The function assumes that the input is of type integer.
    - Large values of n may cause maximum recursion depth errors in a recursive implementation.
    """

    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage and testing of the function
# print(factorial(5))  # Output: 120
# print(factorial(0))  # Output: 1
# print(factorial(3))  # Output: 6


import unittest

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

class TestFactorialFunction(unittest.TestCase):

    def test_basic_functionality(self):
        # Test basic functionality of factorial calculation
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(2), 2)
        
    def test_zero_factorial(self):
        # Test the edge case where n = 0
        self.assertEqual(factorial(0), 1)
        
    def test_one_factorial(self):
        # Test the edge case where n = 1
        self.assertEqual(factorial(1), 1)
        
    def test_large_number(self):
        # Test larger numbers to see if function handles them correctly
        self.assertEqual(factorial(10), 3628800)

    def test_negative_input(self):
        # Test error case where n is a negative number
        with self.assertRaises(ValueError):
            factorial(-5)
            
    def test_non_integer_input(self):
        # Test for non-integer inputs using the isinstance check
        with self.assertRaises(TypeError):
            factorial(5.5)

    def test_string_input(self):
        # Test for string input
        with self.assertRaises(TypeError):
            factorial("test")

# This block is commented out to prevent execution outside of a testing framework
# if __name__ == "__main__":
#     unittest.main()
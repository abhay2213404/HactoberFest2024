# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci series
    for i in range(2, n):
        next_value = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_value)
    
    return fib_sequence

# Input: number of terms
n = int(input("Enter the number of terms: "))

# Output: Fibonacci series
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print([0])
else:
    print(fibonacci(n))

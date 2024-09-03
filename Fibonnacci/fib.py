def fibonacci_iterative(n):
    fib_sequence = [0,1]
    for i in range (2, n):
        next_value = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_value)
    return fib_sequence

n = 10
print(fibonacci_iterative(n))



def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = 10
fibonacci_sequence = [fibonacci_recursive(i) for i in range(n)]
print(fibonacci_sequence)

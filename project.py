def rightmost_set_bit(n):
    if n == 0:
        return None  # No set bits in 0
    return n & -n

# Example usage
number = 18  # Binary: 10010
rightmost_bit = rightmost_set_bit(number)

if rightmost_bit is not None:
    print(f"The rightmost set bit in {number} is: {rightmost_bit} (binary: {bin(rightmost_bit)})")
else:
    print("There are no set bits in the number.")

def find_all_substrings(s):
    """Return all possible substrings of the given string."""
    substrings = []

    # Generate all substrings using nested loops
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])

    return substrings

# Example usage
input_string = "abc"
result = find_all_substrings(input_string)

print(f"All substrings of '{input_string}':")
print(result)

def palindrome(word):
    return word == word[::-1]

def find_positions(input_file):
    positions = {}
    with open("задание 8.txt", 'r') as file:
        for line in file:
            words = line.split()
            for index, word in enumerate(words):
                if palindrome(word):
                    if word in positions:
                        positions[word].append(index)
                    else:
                        positions[word] = [index]
    return positions

input_file = "задание 8.txt"
palindrome_positions = find_positions(input_file)

for word, pos in palindrome_positions.items():
    print(f"Слово '{word}' является полидромом и появляется в позициях: {pos}")
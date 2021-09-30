word = "selfish"
second_word= "fish"
def unique_letters(x) :
    output = [x]
    for char in x:
        if char not in output and char !="":
            output.append(char)
    return output
final_ouput = (unique_letters(word) + unique_letters(second_word))
print(sorted(final_ouput))
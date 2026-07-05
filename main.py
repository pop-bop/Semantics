import random

with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read().strip("\n")
    data = content.split()
    print("Training Data:", data)

temperature = 1

prompt = input("Enter your prompt: ")
prompt = prompt.split()
prompt_last = prompt[-1]

i = 0
while i < 100:
    indices = [index for index, value in enumerate(data) if value == prompt_last]

    next_words_indexes = [x + 1 for x in indices if x + 1 < len(data)]

    next_words = [data[y] for y in next_words_indexes]
    if len(next_words) == 0:
        break

    values = list(dict.fromkeys(next_words))

    weights = [next_words.count(x) ** (1 / temperature) for x in values]

    distribution = random.choices(values, weights=weights, k=1)
    next_token = distribution[0]
    print(next_token, end=' ')

    prompt_last = next_token

    i += 1

print()

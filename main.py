from time import time

prompt = ("A lot of things remind me of my father who passed away when I was 24. "
          "Driving on certain back roads he showed me. Stopping at certain stores he always used to go to. "
          "Eating at his favorite places. More and more of these places are fading away too though. "
          "The roads keep getting built up more and more. The shops and restaurants are closing down. "
          "At first it was heartbreaking that my father wasn't in this world anymore. "
          "But slowly the things that remind me of him are leaving this world as well."
          "The quick brown fox jumps over the lazy dog."
          "Mr. Jock, TV quiz PhD, bags few lynx."
          "Back in my quaint garden, jaunty zinnias vie with flaunting phlox."
          "A quick move by the enemy will jeopardize six fine gun boats.")

def counter():
    print(prompt)
    input(">> Press ENTER to begin")
    begin_time = time()
    inp = input("\n")
    end_time = time()
    final_time = (end_time - begin_time) / 60
    return final_time, inp

def wpm(time_taken, line):
    words = line.split()
    word_length = len(words)
    words_per_m = word_length / time_taken if time_taken > 0 else 0
    return words_per_m

def wordcheck(inp):
    prompts = prompt.split()
    inputs = inp.split()
    errorcount = 0

    idx = 0
    for word in inputs:
        if idx >= len(prompts):
            errorcount += 1
            continue

        if word != prompts[idx]:
            errorcount += 1
        idx += 1

    correct = len(prompts) - errorcount
    percentage = (correct / len(prompts)) * 100
    return percentage

tm, line = counter()
tm = round(tm, 2)
words_per_minute = round(wpm(tm, line), 2)

print(f"Your total time was: {tm} minutes")
print(f"With an average WPM Score of: {words_per_minute} Words Per Minute")

percentage = round(wordcheck(line), 2)
print(f"With an Accuracy of: {percentage}% Accuracy")

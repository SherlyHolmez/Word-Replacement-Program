def replace_word():
    str = "Hello world, It is Shahzeb, I'd just like to say hello hello hello hello"
    print(str)
    word_to_replace = input("Please enter the word to be replaced:")
    word_replacement = input("Please enter the word you would like to replace it with:")
    print(str.replace(word_to_replace,word_replacement))

replace_word()
def print_upper_words(words, must_start_with= {"h","y"}):
    """ 
    turns words to uppercase 
    ex. "hi" => "HI"
    """
    for word in words:
        for letter in must_start_with:
             if  letter == word[0]:
                 print(word)



 
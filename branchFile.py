def main():
    print("Lets prints some words in pig latin. Input strings and we will transform them to big latin.")
    print("To exit program type 'done' Lets begin!")
    word= input("Enter a word: ")
    word=word.lower()
    while(word!="done"):
        print(convertToPigLatin(word))
        print(reverse(word))
        word= input().lower()
    


def findFirstVowel(word):
    end=len(word)
    for index in range(0,end):
        if (word[index]== 'a' or word[index]=='e' or word[index]=='i' or word[index]=='o' or word[index]=='u'):
            return index
    return end-1


def convertToPigLatin(word):
    first=findFirstVowel(word)
    if(first==0):
        word=word+word[0]+"way"
        word=word[1:]
    elif(first!= (len(word)-1)):
        word=word+word[0:first]+"ay"
        word=word[first:]
    else:
        word=word

    return word

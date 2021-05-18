from tkinter import *

browser = Tk()
browser.geometry("691x691")
browser.title('Mad Libs!')

# background image
bg = PhotoImage(file = "bg_image.png")
my_label = Label(browser, image = bg)
my_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

Label(browser, text = "Mad Libs!" , font = "georgia 20 bold").pack()
Label(browser, text = 'Choose your story: ', font = "georgia 15").pack()

#### COMMENTED OUT FOR USER INPUT IMPLEMENTATION ####
##def retrieve_input():
    #inputValue = inputBox.get("1.0","end-1c")
    #print(inputValue)

#def photographer():
    #
    #Button(browser, text = "Enter", font = "arial 15", command = retrieve_input, bg = 'white').place(x = 550, y = 275)
    #Label(browser, text = "Enter your answer here: ", font = "georgia 10").place(x = 390, y = 275)
    #inputBox.place(x = 400, y = 300)
    #adj1 = input("Enter an adjective: ")
    #noun1 = input("Enter a noun: ")
    #print(adj1 + " " + noun1)

#### COMMENTED OUT FOR USER INPUT IMPLEMENTATION ####


def butterfly():

    adj1 = input("enter an adjective: ")
    color = input("enter a color: ")
    thing = input("enter a random thing: ")
    place = input("enter a place: ")
    person = input("enter a person's name: ")
    adj2 = input("enter an adjective: ")
    insect= input("enter a type of insect: ")
    food = input("enter a type of food: ")
    verb = input("enter a verb: ")
    
    finalString = "Last night I dreamed I was a " + adj1 + " butterfly with " + color + " splotches that looked like " + thing + "." + "\n" +  "I flew to " + place + " with my bestfriend " + person + ", who was a " + adj2 + " " + insect + "." + "\n" + "We ate some " + food + " when we got there, and then decided to " + verb + " ." + "\n" + "The dream ended when I said: lets " + verb + "!"
    Label(browser, text = finalString, font = "arial 10", bg = "white").pack(pady = 10)

    Label(browser, text = "Click a new story to play again!", font = "georgia 15", bg = "white").pack()


def apple():

    person = input("enter a person's name: ")
    color = input("enter a color: ")
    food = input("enter a food type: ")
   
    finalString = "Today we picked apple from " + person + "'s Orchard. I had no idea there were so many different varieties of apples." + "\n" + "I ate " + color + " apples straight off the tree that tasted like " + food + "."
    Label(browser, text = finalString, font = "arial 10", bg = "white").pack(pady = 10)

    Label(browser, text = "Click a new story to play again!", font = "georgia 15", bg = "white").pack()

inputBox = Text(browser, height = 1, width = 14)
displayBox = Label(browser)

#photoButton = Button(browser, text = "The Photographer", font = "arial 15", command = photographer, bg = "white").pack(pady = 20)
butterflyButton = Button(browser, text = "The Butterfly", font = "arial 15", command = butterfly, bg = "white").pack(pady = 20)
appleButton = Button(browser, text = "Apple and Apple", font = "arial 15", command = apple , bg = "white").pack()

browser.mainloop()
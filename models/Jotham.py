'''
X Simulator

Model: Jotham
Creator: xiurobert

Original site: https://github.com/xiurobert/jotham-simulator

Parts of original code reused
'''
from time import sleep
from random import randint
from models import randomStartStopConflictException

class Jotham():

    def __init__(self, height = 150, weight = 60, IQ = 100, firstName = "Jotham", surname = "Derp", deathAge = 80,
                 partSize = 30, hotnessLevel = 0):

        '''

        :param height: Height of Jotham in CM int
        :param weight: Weight of Jotham in KG int
        :param IQ: IQ of Jotham int
        :param firstName: Firstname of Jotham str
        :param surname: Surname of Jotham str
        :param deathAge: DeathAge of Jotham int
        :param partSize: Partsize of Jotham int
        :param hotnessLevel: HotnessLevel of Jotham int
        '''

        self.height = height
        self.weight = weight
        self.IQ = IQ
        self.firstName = firstName
        self.surname = surname
        self.deathAge = deathAge
        self.partSize = partSize
        self.hotnessLevel = hotnessLevel

        self.currAge = 0
        self.listOfDates = []
        self.married = False
        self.partner = None

        print("Jotham (" + firstName + " " + surname + ") was created")
        sleep(2)
        print(firstName + ": *wakes up* *rubs eyes* hoowsh... what is this world?")
        sleep(2)
        print("...")

    def addAge(self, years):
        '''

        :param years: Adds years of age to Jotham
        :return: bool Returns either True or False if it was successful or not
        '''

        if self.currAge + years < self.deathAge:
            self.currAge += years
            return True
        else:
            print("Doing this will kill Jotham. Abort.")
            return False

    def instantDeath(self):

        '''
        Immediately kills Jotham
        :return: bool Returns based on whether Jotham was killed or not
        '''

        print(self.firstName + ": Well, it has been nice while it lasted.")
        sleep(2)
        print(self.firstName + ": Goodbye, cruel world.")
        sleep(2)
        print("...")
        del self

    def date(self, personName = "Alyssa", rndStartVal = -10, rndEndVal = 10):
        '''
        Makes Jotham find a date and see if he was successful in dating them
        :param personName: strName of the person Jotham is going to try and date
        :param rndStartVal: int Value of the random date generating seed start range. Affected by hotnessLevel
        :param rndEndVal: int Value of the random date generating seed end range. Affected by hotnessLevel
        :return:
        '''
        print(self.firstName + ": I'm going dating? Oh. That's cool")
        sleep(2)
        print("[MATCHMAKE.COM] The dating system has found a person called " + personName + " !")
        if rndStartVal < rndEndVal:
            if randint(-1 * (rndStartVal + self.hotnessLevel), rndEndVal + self.hotnessLevel) <= self.hotnessLevel:
                print("[MATCHMAKE.COM] Congratulations, " + self.firstName + " , you found a DATE! Their name is: " + personName)
                sleep(2)
                print(self.firstName + ": Oh?")
                self.listOfDates.append(personName)
            else:
                print("[MATCHMAKE.COM] Unfortunately, we were unable to find a match for you. Please try again later")
        else:
            print("The random values inputted are not allowed. Abort and raising exception")
            raise randomStartStopConflictException

    def marry(self, personToMarry):
        '''
        Marries the person to marry
        :param personToMarry: name of person to marry.
        :return:
        '''
        if personToMarry in self.listOfDates:
            print("<Game> Your character will marry " + personToMarry)
            print(self.firstName + ": I'm going to be MARRIED? HURRAY!")
            sleep(5)
            print("2 weeks later...")
            sleep(2)
            print("The sound of wedding bells are heard...")
            sleep(3)
            print("Jotham got married!")
            self.married = True
            self.partner = personToMarry
        else:
            print("<Game> You currently can't marry a person not in the list of dates.")


    def workout(self, rndStrt = 0, rndEnd = 1000):
        '''
        Increase's self's hotness level by a random amount between rndStrt and rndEnd. rndStrt and rndEnd will be
        affected by hotnessLevel
        :param rndStrt: Start of the random generator. Negative values will be made positive
        :param rndEnd: End of the random generator
        :return:
        '''
        if rndStrt < rndEnd:
            newHotness = randint(rndStrt + self.hotnessLevel, rndEnd + self.hotnessLevel)
            print(self.firstName + ": I'm going to work out, I guess")
            self.hotnessLevel += (newHotness - self.hotnessLevel)
        else:
            raise randomStartStopConflictException




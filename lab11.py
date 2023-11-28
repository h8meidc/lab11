import csv

import os

flag = False

try:

    csvfile = open("Lab11.csv","r")

    reader = csv.DictReader(csvfile, delimiter = ",")

    print("Country Name: 2016 [YR2016]")

    for row in reader:

        print(row['Country Name'], ': ', row["2016 [YR2016]"])

    csvfile.close()

except:

    print("Файл Lab11.csv не знайдено!")

try:

    csvfile = open("Lab11.csv","r")

    reader = csv.DictReader(csvfile, delimiter = ",")

    indicator = input("\nВведіть будь-яке значення, щоб знайти показники, які більші цього значення: ")

    while indicator.isalpha():
        print("Значення повинно бути числом")
        indicator = input("Введіть значення ще раз: ")

    os.system('clear')

    print("Country Name: 2016 [YR2016]")

    for row in reader:
        if indicator < row["2016 [YR2016]"]:

            flag = True

            print(row["Country Name"], ": ", row["2016 [YR2016]"])

            with open("new_lab11.csv","a") as csvfile2:

                writer = csv.writer(csvfile2, delimiter = ",")

                writer.writerow((row["Country Name"], row["2016 [YR2016]"]))

    csvfile.close()

    if flag == False:

        os.system('clear')

        print("Показників, які більші, ніж значення, яке ви ввели (" + indicator + ") - немає.")

except:

    print("Файл Lab11.csv не знайдено!")


score = 0
print("Ответь на следующие вопросы:")
questions = ["1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?",
             "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?",
             "3. Как называется капитал, который дают инвесторы на развитие стартапа?",
             "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?",
             "5. Какой план создают перед тем, как открывать стартап и занимать деньги?",
             "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?",
             "7. Как называется разница между выручкой и затратами компании?",
             "8. Столицаа России?"
]
answers = ["Стартап",
            "Инвестор",
            "Инвестиция",
            "MVP",
            "Бизнес-план",
            "Конкуренты",
            "Прибыль",
            "Москва"
]
print(questions[0])
user_input = input("Ввод текста:")


if answers[0].lower() == user_input.lower():
    print("правильно")
    score = score + 1
else:
    print("неправильно")

print(score)

print(questions[1])
user_input = input('Ввод текста:')
if answers[1].lower() == user_input.lower():
    print("правильно")
    score += 1
else:
    print("неправильно")
    print(score)

print(questions[2])
user_input = input("Ввод текста:")
if user_input.lower() == answers[2].lower():
    print('Правильно!')
    score += 1
else:
    print('Неправильно.')
print(score)

print(questions[3])
user_input = input("Ввод текста:")
if user_input.lower() == answers[3].lower():
    print('Правильно!')
    score += 1
else:
    print('Неправильно.')
print(score)

print(questions[4])
user_input = input("Ввод текста:")
if user_input.lower() == answers[4].lower():
    print('Правильно!')
    score += 1
else:
    print('Неправильно.')
print(score)

print(questions[5])
user_input = input("Ввод текста:")
if user_input.lower() == answers[5].lower():
    print('Правильно!')
    score += 1
else:
    print('Неправильно.')
print(score)

print(questions[6])
user_inputs = input("Ввод текста:")
if user_input.lower() == answers[4].lower():
    print('Правильно!')
    score += 1
else:
    print('Неправильно.')
    print(score)
print(questions[7])
user_input = input("Ввод текста:")
if user_input.lower() == answers[7].lower():
    print('Правильно!')
    score += 1
else:
    print('Неправильно.')
    print(score)

print("спасибо!")

if score == 8:
    print("Молодец!")
elif score > 5:
    print("Нормально")
elif score > 3:
    print("Неплохо")
elif score > 0:
    print("Плохо")
else:
    print("Ужасно")

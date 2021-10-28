
define e = Character("Ао")

label start:

    scene classroom

    show hello


    e "Приветствую тебя в нашей Школе Криптографии! "

    hide hello

    show normal

    e "Я Ао, местный учитель, директор и владелец Школы"

    e "Здесь ты научишься основам криптографии и узнаешь много интересного."

    e "Давай я объясню тебе, как проходит обучение."

    e "Сначала мы тебе расскажем, как работает тот или иной шифр, а потом дадим несколько не очень сложных заданий."

    hide normal

    show ugol

    e "Чтобы тебе было проще, тебе дадут справочник, он находится тут"

    hide ugol

    show normal

    e "Ты всегда можешь посмотреть нужную информацию в нем."

    e "Кстати, не забудь вернуть его в библиотеку."

    e "После прохождения обучения ты пройдёшь последнее испытание, где мы проверим твои знания."

    e "У тебя есть какие-то вопросы?"
    hide normal

    menu:
        "У тебя есть какие-то вопросы?"

        "нет":
            jump caesar

        "Что такое криптография?":

            show clever

            e "Криптография — это наука о способах и методах шифрования информации. Она защищает передаваемые сообщения и использует опробованные в открытых средах алгоритмы, которые позволяют быстро обнаруживать и устранять любые уязвимости."

            e "Вот что тебе скажет интернет, если его спросить."

            e "На самом деле то очень древняя наука, которая служит для защиты информации."

            e "Раньше это бы всего лишь простые шифры, но с приходом современных технологий все усложнилось, сейчас люди научились создавать такие методы шифрования, что не каждый сможет разобраться."

            hide clever

            menu:
                "Еще остались вопросы?"

                "Вопросов больше нет":
                    jump caesar
                "Долго ли мне нужно учиться?":
                    show normal
                    e "Тут не так много уровней, думаю, ты быстро справишься."

                    hide normal
                    menu:
                        "Еще остались вопросы?"
                        "Вопросов больше нет":
                            jump caesar
                        "Что еще за испытание?":
                            show clever
                            e "Ты будешь выполнять задания, как в уровнях, но без Справочника и с ограниченным временем."
                            hide clever
                            jump caesar
                "Что еще за испытание?":
                    show clever
                    e "Ты будешь выполнять задания, как в уровнях, но без Справочника и с ограниченным временем."
                    hide clever
                    menu:
                        "Еще остались вопросы?"
                        "Вопросов больше нет":
                            jump caesar
                        "Долго ли мне нужно учиться?":
                            show normal
                            e "Тут не так много уровней, думаю, ты быстро справишься."
                            hide normal
                            jump caesar
        "Долго ли мне нужно учиться?":
            show normal
            e "Тут не так много уровней, думаю, ты быстро справишься."
            hide normal
            menu:
                "Еще остались вопросы?"

                "Вопросов больше нет":
                    jump caesar
                "Что такое криптография?":
                    show clever
                    e "Криптография — это наука о способах и методах шифрования информации. Она защищает передаваемые сообщения и использует опробованные в открытых средах алгоритмы, которые позволяют быстро обнаруживать и устранять любые уязвимости."

                    e "Вот что тебе скажет интернет, если его спросить."

                    e "На самом деле то очень древняя наука, которая служит для защиты информации."

                    e "Раньше это бы всего лишь простые шифры, но с приходом современных технологий все усложнилось, сейчас люди научились создавать такие методы шифрования, что не каждый сможет разобраться."
                    hide clever
                    menu:
                        "Еще остались вопросы?"

                        "Вопросов больше нет":
                            jump caesar

                        "Что еще за испытание?":
                            show clever
                            e "Ты будешь выполнять задания, как в уровнях, но без Справочника и с ограниченным временем."
                            hide clever
                            jump caesar
                "Что еще за испытание?":
                    show clever
                    e "Ты будешь выполнять задания, как в уровнях, но без Справочника и с ограниченным временем."
                    hide clever
                    menu:
                        "Еще остались вопросы?"

                        "Вопросов больше нет":
                            jump caesar
                        "Что такое криптография?":
                            show clever
                            e "Криптография — это наука о способах и методах шифрования информации. Она защищает передаваемые сообщения и использует опробованные в открытых средах алгоритмы, которые позволяют быстро обнаруживать и устранять любые уязвимости."

                            e "Вот что тебе скажет интернет, если его спросить."

                            e "На самом деле то очень древняя наука, которая служит для защиты информации."

                            e "Раньше это бы всего лишь простые шифры, но с приходом современных технологий все усложнилось, сейчас люди научились создавать такие методы шифрования, что не каждый сможет разобраться."
                            hide clever
                            jump caesar

        "Что еще за испытание?":
            show clever
            e "Ты будешь выполнять задания, как в уровнях, но без Справочника и с ограниченным временем."
            hide clever
            menu:
                "Еще остались вопросы?"

                "Вопросов больше нет":
                    jump caesar
                "Что такое криптография?":
                    show clever
                    e "Криптография — это наука о способах и методах шифрования информации. Она защищает передаваемые сообщения и использует опробованные в открытых средах алгоритмы, которые позволяют быстро обнаруживать и устранять любые уязвимости."

                    e "Вот что тебе скажет интернет, если его спросить."

                    e "На самом деле то очень древняя наука, которая служит для защиты информации."

                    e "Раньше это бы всего лишь простые шифры, но с приходом современных технологий все усложнилось, сейчас люди научились создавать такие методы шифрования, что не каждый сможет разобраться."
                    hide clever
                    menu:
                        "Еще остались вопросы?"

                        "Вопросов больше нет":
                            jump caesar
                        "Долго ли мне нужно учиться?":
                            show normal
                            e "Тут не так много уровней, думаю, ты быстро справишься."
                            hide normal
                            jump caesar
                "Долго ли мне нужно учиться?":
                    show normal
                    e "Тут не так много уровней, думаю, ты быстро справишься."
                    hide normal
                    menu:
                        "Еще остались вопросы?"

                        "Вопросов больше нет":
                            jump caesar
                        "Что такое криптография?":
                            show clever
                            e "Криптография — это наука о способах и методах шифрования информации. Она защищает передаваемые сообщения и использует опробованные в открытых средах алгоритмы, которые позволяют быстро обнаруживать и устранять любые уязвимости."

                            e "Вот что тебе скажет интернет, если его спросить."

                            e "На самом деле то очень древняя наука, которая служит для защиты информации."

                            e "Раньше это бы всего лишь простые шифры, но с приходом современных технологий все усложнилось, сейчас люди научились создавать такие методы шифрования, что не каждый сможет разобраться."
                            hide clever
                            jump caesar

    return

label caesar:
    e "Раз вопросов нет, то начнем наше обучение!"

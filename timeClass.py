# noinspection PyTypeChecker
class Time:

    def __init__(self, hour=12, minute=30, second=15):
        self.__hour = 1
        self.__minute = 0
        self.__second = 0
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if isinstance(hour, int) and 0 <= hour <= 23:
            self.__hour = hour
        else:
            print("hour Error")

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        if isinstance(minute, int) and 0 <= minute < 60:
            self.__minute = minute
        else:
            print("minute Error")

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second):
        if isinstance(second, int) and 0 <= second < 60:
            self.__second = second
        else:
            print("second Error")

    def __str__(self):
        if 0 <= self.hour <= 12:
            return f"{self.hour:02}:{self.minute:02}:{self.second:02} AM"
        elif 12 < self.hour <= 23:
            return f"{self.hour - 12:02}:{self.minute:02}:{self.second:02} PM"

    def tik(self):
        self.__second += 1
        if self.__second == 60:
            self.__minute += 1
            self.__second = 0
            if self.__minute == 60:
                self.__minute = 0
                self.__hour += 1
                if self.__hour == 24:
                    self.__hour = 0

    def is_midnight(self):
        return self.__hour == 0 and self.__minute == 0 and self.__second == 0

    def __next__(self):
        self.tik()
        if self.is_midnight():
            print("it's midnight")
        return self

    def run(self):
        def clear():
            from os import system
            system('cls')
        from time import sleep
        while True:
            print(next(self))
            sleep(1)
            clear()


if __name__ == "__main__":
    t1 = Time(23, 59, 57)
    t1.run()

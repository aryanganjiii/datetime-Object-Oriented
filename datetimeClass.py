from timeClass import Time


class Date(Time):
    numOfDays = [0, 31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 30]

    def __init__(self, year=1400, month=1, day=1, hour=1, minute=1, second=1):
        self.__year = 1
        self.__month = 1
        self.__day = 1
        self.year = year
        self.month = month
        self.day = day
        Time.__init__(self, hour, minute, second)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if isinstance(year, int) and year > 0:
            self.__year = year
        else:
            print('year error')

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if isinstance(month, int) and 0 < month < 13:
            self.__month = month
        else:
            print('month error')

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if isinstance(day, int) and 0 < day <= self.numOfDays[self.month]:
            self.__day = day
        else:
            print('day error')

    def __str__(self):
        return f"{self.year:04}/{self.month:02}/{self.day:02} | " + super(Date, self).__str__()

    def tik(self):
        super().tik()
        if self.hour==0 and self.minute==0 and self.second==0:
            self.__day += 1
            if self.__day == self.numOfDays[self.month] + 1:
                self.__day = 1
                self.__month += 1
                if self.__month == 13:
                    self.__month = 1
                    self.__year += 1

    def is_new_year(self):
        return self.day == 1 and self.month == 1

    def __next__(self):
        self.tik()
        if self.is_midnight():
            print("it's midnight")
        if self.is_new_year():
            print("happy new year")
        return self


if __name__ == "__main__":
    d1 = Date(1380, 2, 31, 23, 59, 58)
    d1.run()
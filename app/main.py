class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        diffence = self.clean_power - car.clean_mark
        total = car.comfort_class * diffence * self.average_rating
        income = total / self.distance_from_city_center
        return income

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        sum_of_incomes = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                sum_of_incomes += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(sum_of_incomes, 1)

    def rate_service(self, rate: int) -> None:
        all_rate = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(all_rate / self.count_of_ratings, 1)

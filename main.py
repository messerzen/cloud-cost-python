import calendar


class CloudCost():
    """This class calculates the final cost of a serverless operation."""

    def __init__(self):
        self.n_funct = 2
        self.cost_msg = 0.00000040
        self.cost_funct = 0.0000002
        self.cost_time = 0.0002080
        self.time_sec = 3

    def lambda_execution(self):
        cost_func = self.cost_funct + (self.cost_time*self.time_sec)
        return cost_func

    def app_execution(self, execution_times):
        unit_cost = self.lambda_execution()
        cost_req = ((unit_cost*self.n_funct) + self.cost_msg) * execution_times
        return cost_req

    def month(self, execution_times, month_of_year):
        unit_cost =  self.app_execution(execution_times)
        days_month = calendar.monthrange(2019, month_of_year)[-1]
        cost_month = unit_cost * days_month
        return cost_month
    
    def year(self, execution_times):
        anual_cost = []

        for n_days in range(1,13):
            monthly_cost = self.month(execution_times, n_days)
            anual_cost.append(monthly_cost)
        return anual_cost

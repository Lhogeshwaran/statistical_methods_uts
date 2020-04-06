import math

class Eda:

    def __init__(self, ls):

        self.ls = ls
        self.sample_size = len(ls)

class Distance(Eda):

    def __init__(self, ls):
        
        Eda.__init__(self, ls)
        self.mean = self._mean()
        self.var = self._var()
        self.sd = self._sd()

    def _mean(self):

        sum_tmp = 0
        for i in self.ls:
                sum_tmp = sum_tmp + i

        return round(sum_tmp/len(self.ls), 2)

    def mean(self):

        val = self._mean()
        return val

    def _var(self):

        tmp_mean = self._mean()

        tmp_sum = 0
        for i in self.ls:
                tmp_sum = tmp_sum + ((i - tmp_mean)**2)

        return round(tmp_sum/(len(self.ls)-1), 2)

    def _sd(self):

        tmp_var = self._var()
        return round(math.sqrt(tmp_var), 2)

class Distance2:

    def __init__(self):
        self.mean = self.mean()

    def mean(ls):

        sum_tmp = 0
        for i in ls:
                sum_tmp = sum_tmp + i

        return round(sum_tmp/len(ls), 2)

    def var(self, ls):

        tmp_mean = self.mean()
        
        tmp_sum = 0
        for i in ls:
                tmp_sum = tmp_sum + ((i - tmp_mean)**2)

        return round(tmp_sum/(len(self)-1), 2)

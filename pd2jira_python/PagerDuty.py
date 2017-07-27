from BaseClass import BaseClass


class PagerDuty(BaseClass):

    @staticmethod
    def is_triggered_alert(data):
        try:
            return data['incident']['status'] == 'triggered'
        except:
            return False

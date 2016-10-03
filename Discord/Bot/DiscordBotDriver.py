import datetime
import logging

#TODO
# *Change if statement to account for day.
# *Set target time for post. might have to get hour and minute
# *write discord object
# connect it to this one.
# test

class Driver:
    def __init__(self):
        # Create logger
        self.logger = self.createLogger()

        # Setting the variables
        self.numberOfCorrect = 0
        self.baseTarget = datetime.datetime.now()
        self.baseTarget = self.baseTarget.replace(second=0, microsecond=0)

    def createLogger(self):
        # create logger
        logger = logging.getLogger('DiscordBotDriver')
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to DEBUG
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        # returns logger
        return logger

    def runner(self):
        self.logger.info("baseTarget: " + str(self.baseTarget))

        # The current target is 5 minutes ahead of the base target
        currentTarget = self.baseTarget + datetime.timedelta(minutes=5)

        self.logger.info("currentTarget: " + str(currentTarget))
        self.logger.info("Starting Loop")

        while(self.numberOfCorrect < 5):
            # Get the current time
            current = datetime.datetime.now()

            # If the current time is ahead the current target
            # then we execute the function
            if (current >= currentTarget):
                self.numberOfCorrect += 1
                currentTarget = currentTarget + datetime.timedelta(minutes=5)

                self.logger.info("It worked")
                self.logger.info("New current target is: " + str(currentTarget))
                self.logger.info(self.numberOfCorrect)

        logging.info("out of the loop")

driver = Driver()
driver.runner()

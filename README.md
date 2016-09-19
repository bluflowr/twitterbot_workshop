
# Simple Twitter bot

This project takes random Dr Seuss quotes and tweets them out.

## APIs Used

###[Twitter](https://dev.twitter.com/)  

## Installation

### 1. virtualenv

Learn more about [virtualenv](http://www.virtualenv.org/). Create a new virtualenv for your own project, where `projectname` is the name of your project:

`$ virtualenv --python=python3 projectname`

Activate your virtualenv:

`$ source projectname/bin/activate`

### 2. Download
Now, you need the *twitterbot_workshop* project files in your environment:

    $ cd /path/to/your/project
    $ git clone git://github.com/bluflowr/twitterbot_workshop.git projectname && cd projectname

### 3. Requirements
Included is the *requirements.txt* file that has all the resources you'll need for this project. To install them, simply type:

`$ pip install -r requirements.txt`  

### 4. SECRET_KEY and Credentials
Rename `secret_example.py` to `secret.py`

Go to [Twitter](https://apps.twitter.com/). Once you've created you app keys and access tokens, enter your Twitter credentials in `secret.py`.


### 5. Twitter Cron Job

Create a cron job to post updates to twitter. Example for posting at 5am and 5pm.

	$ 0 5,17 * * * cd /Path/to/your/code && source YOURenv/bin/activate && python tweet.py -p

## Implementation
Bot updates post to [@pyladiesatx_bot](https://twitter.com/pyladiesatx_bot)
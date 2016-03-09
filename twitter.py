import tweepy
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

ckey='KabIDa9OWkF99x0qvjK5HDDY6'
csecret='5kcRwKI6JMlUYlf5DWGFmuYC9QQgDniz1nh42TrNmVxYAayxaL'
atoken='4871567865-t5WSvs6FXolO4GWFpydN3K7R76acLALwPnctxvl'
asecret='purlpm8qc8WxDWmCZm7sLUY6y4QKF1iJBmY9sv5JuzYkI'

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)

u1 = raw_input('give me the first user: \n')
u2 = raw_input('give me the second user: \n')
try:
	user1 = api.get_user(u1)
	user2 = api.get_user(u2)

	n1 = user1.screen_name
	n2 = user2.screen_name
	f1 = user1.followers_count
	f2 = user2.followers_count
	st1 = user1.statuses_count
	st2 = user2.statuses_count
	fr1 = user1.friends_count
	fr2 = user2.friends_count
	fav1 = user1.favourites_count
	fav2 = user2.favourites_count

	sc1=0 
	sc2=0

	if f1 >= f2:
		sc1 = sc1 +1
		sc2 = sc2  
	else:
		sc1 = sc1  
		sc2 = sc2 + 1
	if st1 >= st2:
		sc1 = sc1 + 1
		sc2 = sc2  
	else:
		st1 = sc1  
		sc2 = sc2 + 1
	if fr1 >= fr2:
		sc1 = sc1 + 1
		sc2 = sc2  
	else:
		sc1 = sc1  
		sc2 = sc2 + 1
	if fav1 >= fav2:
		sc1 = sc1 + 1
		sc2 = sc2  
	else:
		sc1 = sc1  
		sc2 = sc2 + 1
		
	print '--> Profile: ',n1,': TWEETS:',st1,' FOLLOWING:',fr1,' FOLLOWERS:',f1,' LIKES:',fav1,'\n'
	print '--> Profile: ',n2,': TWEETS:',st2,' FOLLOWING:',fr2,' FOLLOWERS:',f2,' LIKES:',fav2,'\n'	
	print 'Score: ',sc1 ,' - ', sc2 
except:
	print 'not found the first or/and second user,Try again!'
## **Task 1 Software configuration.**
### Subtask1 ***"Why did I choose to participate in the challenge portfolio?”***

I decided to participate in the challenge for the following reasons:
> 1.  It has always been interesting to find out how the system works from the inside.
> 
> 2. I have such a character trait that allows me to fully understand the issue that interests me.
> 3. I really like to communicate with people.
> 
When I saw the opportunity to take part in the Dare it "Portfolio Challenge" contest, I realized that I needed it to gain experience
which I don't have. And I filled out the participant's questionnaire and was looking forward to getting the knowledge faster. I hope to become the best of all the participants of the challenge, and in the future I will be able to apply this knowledge in practice.

## **Task 1 Налаштування програмного забезпечення.**
### Subtask1 ***"Чому я вирішив взяти участь у конкурсі challenge portfolio??”***

Я вирішив взяти участь у конкурсі з наступних причин:
> 1.  Завжди було цікаво дізнатися, як працює система зсередини.
> 
> 2. У мене є така риса характеру, яка дозволяє мені повністю розібратися в питанні, що цікавить мене.
> 3. Мені дуже подобається спілкуватися з людьми.


Коли я побачив можливість взяти участь у конкурсі Dare IT "Portfolio Challenge", я зрозумів, що мені це потрібно, щоб отримати досвід
, якого у мене немає. І я заповнив анкету учасника i з нетерпінням чекав можливості швидше отримати знання. Я сподіваюся стати кращим з усіх учасників челенджу, і в майбутньому я зможу застосувати отримані знання на практиці.


## **Task 2 Selectors.**
### Subtask1 ***"Searching for selectors on the login pageList all the elements that are on the login page?”***

***login_field_xpath***
>1.  //*[@id="login"]
>2. //*[@name="login"]
>3. //*[@type="text"]

***password_field_xpath***
>1. //*[@id="password"]
>2. //*[@name="password"]
>3. //*[@type="password"]


***remind_password_xpath***
>1. //*[@id="__next"]/form/div/div[1]/a
>2. //*[text()='Remind password']
>3. //*[@tabindex="-1"]

***language_xpath***
>1. //*[@role="button"]
>2. //*[@aria-haspopup="listbox"]
>3. //*[@tabindex="0"]


***sign_in_button_xpath***
>1.  //*[@class="MuiButton-label"]  
>2.  //*[@id="__next"]/form/div/div[2]/button/span[1]  
>3.  //*[text()='Sign in']

### Subtask 2 ***"Adding selectors to project”***
**login_page.py**
>class LoginPage(BasePage):  
> login_field_xpath = "//*[@id='login']"  
> password_field_xpath = "//*[@id="password']"  
> sign_in_button_xpath = "//*[text()= 'Sign in']"  
> language_xpath = "//*[@role="button']"  
> sign_in_button_xpath = "//*[@class="MuiButton-label"]"  


### Subtask 3 ***"Adding a new file”***
**dashboard.py**
> button_xpath = "//*@id='login']"  
> home_page_xpath = "//*[text()='Main page']"  
> page_Players_xpath = "//*[text()='Players']"  
> language_switching_xpath = "//*['@id="__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"  
> add_player_button_xpath = "//*[text()='Add player']"  
> super_man_button_xpath = "//*[text()='super man']"  
> futbol_kolektyw_logo_xpath = "//*['@title="Logo Scouts Panel']"  
> Dev_team_contact_button_xpath = "//*[text()='Dev team contact']"  
> Players_count_xpath = "//*[text()='Players count']"  
> Matches_count_xpath ="//*[text()='Matches count']"  
> Reports_count_xpath = "//*[text()='Reports count']"  
> Events_count_xpath = "//*[text()='Events count']"  
<h1 id="facebook-birthday-bot">Facebook Birthday Bot</h1>
<p><strong>Automatically wish happy birthday to your facebookfriends</strong>. How to automatically wish happy birthday to friends on Facebook?</p>
<p>You are right here. This is a tiny python3 project.</p>
<p>Install <strong>Python3 on the OS</strong> of your choice. (How to do this? <a href="https://realpython.com/installing-python/">https://realpython.com/installing-python/</a>) Navigate into the folder of your choice and</p>
<pre><code>git clone https://github.com/catchpi/Facebook-Birthday-Bot.git
</code></pre>
<p>Install the requirements.txt by (make sure to have pip3 installed <a href="https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3">https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3</a>)</p>
<pre><code>cd Facebook-Birthday-Bot
pip3 install -r requirements.txt
</code></pre>
<p>Now its time for the Chromedriver.</p>
<pre><code>
CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`
wget http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip 
mkdir /assets
sudo mv chromedriver /assets
sudo chmod +x /assets/chromedriver
rm -rf chromedriver_linux64.zip
</code></pre>
<p>I assume you have installed Chrome, if not use this:</p>
<pre><code>sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" &gt;&gt; /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
</code></pre>
<h1 id="lets-use-the-automatically-facebook-birthday-wisher-bot">Let’s use the automatically Facebook Birthday Wisher Bot</h1>
<p>By default the bot comes with 3 features within the <em><strong><a href="http://config.py">config.py</a></strong></em> file</p>
<pre><code>headless = True
tag = True
telegram = True
</code></pre>
<p>That means if you don’t want to run it headless set it to False, same goes for tagging (by default the bot tags the people it wishes happyBirthday to) and telegram. The bot sends you automatically the name of the person to your telegram (how to set this up later more).</p>
<p><strong>For Login:</strong><br>
Use your Email and Password to login.<br>
Insert your logincreds. PLEASE use your facebook email or it will fail</p>
<pre><code>user =  ''
passwd =  ''
</code></pre>
<h2 id="automates-facebook-birthday-messages">Automates Facebook Birthday Messages</h2>
<p>The Facebook Birthday Bot comes with <em><strong>4 Parts</strong></em> in python lists. Here you can edit your wishes to your loved ones. The structure when <code>Tag = True</code> is <strong>Tagged Person + Hello + Opener + Wish + Good Bye</strong></p>
<p>You can edit these <em><strong>4 Parts</strong></em> and turn off <strong>Tagged Person</strong> by setting <code>tag = False.</code><br>
How to edit the 4 Parts? Just change them and in the randomizer edit the length. In case you just want to use 3 or 5 (for example) edit the <code>greetings_mix = [part1, part2, part3, part4]</code> list add or delete your next greetings list.</p>
<h2 id="how-to-get-notfiyed-whom-you-wished-automatically-happy-birthday">How to get notfiyed whom you wished automatically happy birthday?</h2>
<p>Now use your telegram bot.</p>
<h3 id="creating-your-bot-for-your-facebook-happy-birthday-wisher-bot.">Creating your bot for your facebook happy birthday wisher bot.</h3>
<ol>
<li>On Telegram, search @BotFather, send him a “<strong><em>/start</em></strong>” message</li>
<li>Send another “<strong><em>/newbot</em></strong>” message, then follow the instructions to setup a name and a username</li>
<li>Your bot is now ready, be sure to save a backup of your API token, and correct, this API token is your  <code>bot_token</code></li>
</ol>
<p><img src="https://miro.medium.com/max/60/1*0BCjLBC367cPPmPfFFbuZQ.png?q=20" alt=""></p>
<p><img src="https://miro.medium.com/max/1314/1*0BCjLBC367cPPmPfFFbuZQ.png" alt=""></p>
<p>The part blurred in blue is where you will find your API <strong>bot_token</strong></p>
<h2 id="getting-your-chat-id"><strong>Getting your Chat id</strong></h2>
<ul>
<li>On Telegram, search your bot (by the username you just created), press the “Start” button or send a “<strong><em>/start</em></strong>” message</li>
<li>Open a new tab with your browser, enter  <code>https://api.telegram.org/bot&lt;yourtoken&gt;/getUpdates</code>  , replace  <code>&lt;yourtoken&gt;</code>  with your API token, press enter and you should see something like this:</li>
</ul>
<blockquote>
<pre><code>{"ok":true,"result":[{"update_id":77xxxxxxx,  
"message":{"message_id":550,"from":{"id":34xxxxxxx,"is_bot":false,"first_name":"Man &gt; Hay","last_name":"Hong","username":"manhay212","language_code":"en-HK"}
</code></pre>
</blockquote>
<p>Look for “id”, for instance, 34xxxxxxx above is my chat id. Look for yours and put it as your  <code>bot_chatID</code>  in the code above</p>
<p>Now you are all set, run the code, and enjoy receiving messages from yourself :)</p>
<p>Source: <a href="https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e">@ManHay_Hong</a> Thanks.</p>
<p>Feel free to fork or write me ideas. <a href="mailto:becomebasti@gmail.com">becomebasti@gmail.com</a></p>
<blockquote>
<p><strong>Disclaimer</strong>: Please Note that this is a research project. I am by no means responsible for any usage of this tool. Use on your own behalf. I’m also not responsible if your accounts get banned due to extensive use of this tool. <strong>License GNU GPLv3</strong></p>
</blockquote>


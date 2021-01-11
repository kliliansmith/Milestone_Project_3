<h2>Keto Recipe Handbook</h2>
<p>The purpose of the site is to provide a new person, who has never heard of the keto diet before, with information, recipes and starter meal plans to follow in order to start a keto lifestyle.</p>
<p>The website will allow the user to browns the main home page and recipe list without having to register.</p>
<p>When they are comfortable with a keto diet they can register and add their own recipes and mealplans to the site for others to follow.</p>

<h2>User Experience (UX)</h2>
<ul>
<li><h4>First Time Visitor Goals</h4></li>
<ol>
<li>As a First Time Visitor, I want to be able to find out information on a keto diet easily.</li>
<li>As a First Time Visitor, I want information to be displayed clearly and precisely.</li>
</ol>
<li><h4>Returning Visitor Goals</h4></li>
<ol>
<li>As a Returning Visitor, I want to be able to register and add my own recipes and mealplans to the site.</li>
<li>As a Returning Visitor, I want to be able to access their social media accounts in order to connect with other users of the site.</li>
</ol>
<li><h4>Frequent User Goals</h4></li>
<ol>
<li>As a Frequent User, I want to be able to delete or edit my recipes/mealplans if I have changed anything.</li>
</ol>
</ul>

<h3>Design</h3>
<ul>
<li><h4>Colour Scheme - Main Colours</h4></li>
<ol>
<li>Teal Boxes</li>
<li>White Text for hav and headings</li>
<li>Teal text for the mobile nav heading</li>
<li>Black text for the recipe, mealplan and mobile nav menu</li>
</ol>

<li><h4>Typography</h4></li>
<ul>
<li>For the Nav bar and headings I used Yusei Magic, which is a clean and easy to read font thats different from the bog standard sans-serif</li>
<li>Cormorant Garamond is used for the main body of text within any cards. Such as the recipes, mealplans and home page info.</li>
<li>Sans Serif is used as the fallback font in case for any reason the font isn't being imported into the site correctly.</li>
</ul>

<li><h4>Imagery</h4></li>
<ul>
<li>I have used one image within an image card to display the foods that are allowed to be consumed on a keto diet.</li>
</ul>

<h3>Wireframes</h3>
<li>As there is no where within the module that states how to link wireframes, and google doesnt seem to give a direct answer. Please see the folder included within the project for wireframes.</li>

<h2>Features</h2>
<ul>
<li>Responsive on all device sizes. Please see screenshot folder to the left.</li>
<li>Registration form that checks if a user has already used that name and displays a flash message.</li>
<li>Adding, deleting and editing recipes/mealplans a user has added.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
<li>HTML5</li>
<li>CSS3</lili>
<li>Javascript</li>
<li>Python+Flash</li>
<li>Mongodb</li>
<li>Heroku</li>
<li>Jinja</li>
<li>Materialize</li>
</ul>

<h2>Testing</h2>
<li>The below Services were used to validate every page of the project to ensure there were no syntax errors. Please see Validation and Wireframe Images for results.</li>
<ul>
<li>W3C HTML Validator - https://validator.w3.org</li>
<li>W3C CSS Validator - https://jigsaw.w3.org/css-validator</li>
<li>JavaScript Validator - https://jshint.com</li>
<li>Python Validator - http://pep8online.com</li>
</ul>

<h3>Testing User Stories from User Experience (UX) Section</h3>
<h4>First Time Visitor Goals</h4>
<li>As a First Time Visitor, I want to be able to find out information on a keto diet easily.</li>
<ul>
<li>When visiting the main homepage to the site, it is easy to read with a simple layout.</li>
<li>The image cards are spaced out nicely, text is readable with correct spacing.</li>
<li>The navigation is simple to follow and accessible from both desktop and mobile devices.</li>
<li></li>
</ul>
<br>
<li>As a First Time Visitor, I want information to be displayed clearly and precisely.</li>
<ul>
<li>As mentioned above the cards are easy to read, with simple looking text and font.</li>
<li>Very minimal colours are used throughout the website.</li>
<li>There is only one image used, which is there to provide information to the user.</li>
</ul>
<br>
<h4>Returning Visitor Goals</h4>
<li>As a Returning Visitor, I want to be able to register and add my own recipes and mealplans to the site.</li>
<ul>
<li>The navigation is easy to follow and register is clearly visible for the user to see.</li>
<li>The registratation form will alert the user if the name they have typed is already taken.</li>
<li>The add recipe form will alert the user to when their recipe has been added.</li>
<li>All forms will required a certain amount of text per box before it can be submitted.</li>
</ul>
<br>
<li>As a Returning Visitor, I want to be able to access their social media accounts in order to connect with other users of the site.</li>
<ul>
<li>All social links can be found at the bottom of all pages within the footer of the site.</li>
</ul>

<h4>Frequent User Goals</h4>
<li>As a Frequent User, I want to be able to delete or edit my recipes/mealplans if I have changed anything.</li>
<ul>
<li>Only a registered user will have the edit and delete options available.</li>
<li>The edit and delete options are only available to recipes and meal plans that the user has added.</li>
</ul>

<h3>Further Testing</h3>
<li>The Website has been tested on Google Chrome, Internet Explorer, Microsoft Edge, Safari and Android based browsers.</li>
<li>The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX through the use of both personal items and inspection of the page. Please see screen shots to the left.</li>
<li>Friends were asked to review the site and documentation to point out any bugs and/or user experience issues as well as ensure the pages had linked properly when accessing them.</li>

<h3>Known Bugs</h3>
<li>Sometimes the containers are not always centralised on desktop. This may be due to the fact I have a 32inch 2K monitor though.</li>
<li>Sometimes the site link needs to be refreshed once to display on any device. This is not all the time.</li>
<li>Not always responsive on all devices, sometimes the title drops down. This only happens sometimes.</li>

<h2>Deployment</h2>
<h3>Heroku</h3>
<p>The project was deployed to Keroku via the following steps:</p>
<ol>
<li>Log in to Heroku, create project and ensure this is the same name as on github.</li>
<li>Go to settings and add in appropriate Config Vars. DB name, DB URI, port,secret key and IP.</li>
<li>SGO to deploy, connect to github and select automatic deploys from master.</li>
<li>Ensure master branch is selected.</li>
<li>All git pushes will be deployed to Heroku.</li>
</ol>

<h2>Credits</h2>
<h3>Code and ReadMe Layout</h3>
<li>Code-Institute Modules - mainly data centric mini project for code and code layout.</li>
<li>https://www.healthline.com/nutrition/keto-diet-meal-plan-and-menu#meal-plan for the meal plans.</li>
<li>https://www.dietdoctor.com/low-carb/keto/recipes for the recipes within the website.</li>
<li>ruled.me for a link to their keto guide.</li>
<li>Code-Institude-Solutions/SampleREADME</li>
<li>Materalize for the containers, layout, navbar and cards used throughout as well as linking to font awesome.</li>

<h3>Content</h3>
<li>Information used from various keto websites, as listed above.</li>

<h3>Media</h3>
<li>Any images were taken from google under fair useage rights.</li>

<h3>Acknowledgements</h3>
<li>My Mentor for continuous helpful feedback and helping me understand any mistakes</li>
<li>Slack group users for further my understanding of anything I didnt understand during the mofule.</li>
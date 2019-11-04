# OC_project8

The Pur Beurre start-up, which you have already worked for, decided to launch a web application that would allow their customers to find 
healthy alternatives to food considered "too fat, too sweet, too salty"

## Functionalities

 - Viewing the search field from the home page
 - The search must not be using AJAX
 - Responsive interface
 - The client can create a user account and login/logout
 
 The user will have in one click find a substitute product. He can open a personal space where he can save his backups and find
 them later by logging into his account.
 
 ## Importante note
 
 The algorithm responsible for recovering a substitute is not perfect. Indeed, to find a substitute the program will look for 
 the categories in which the product belongs and then try to find a substitute for the category that contains the least product.
 
 So if we take, for example, the product "Kiri à la crème de lait (12 Portions)" 
 (https://fr.openfoodfacts.org/produit/3073780258098/kiri-a-la-creme-de-lait-12-portions) the program will look for a substitute
 in the "Gouter" category (https://fr-en.openfoodfacts.org/category/gouter) so it could offer us "Grany cereal chocolate" 
 as a substitute, which is not really a substitute.

For the product "Kiri à la crème de lait (12 Portions)" he will not offer us "Grany cereals chocolate" since he does not 
have a better nutri_score but I gave an example to know that it can happen for other products

## Link

You can visit the website at the following address: https://purbeurre-oc8.herokuapp.com/


If you find an error on the website or need help please contact me on: cinorouizi@hotmail.fr or on facebook search: Yacine Rouizi.

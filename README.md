1.1 Routes
http://localhost:8000/ - Home page
· http://localhost:8000/recipe/catalogue/ - Catalogue page
· http://localhost:8000/recipe/create/ - Recipe create page
· http://localhost:8000/recipe/<recipe_id >/details/ - Recipe details page
· http://localhost:8000/recipe/<recipe_id >/edit/ - Recipe edit page
· http://localhost:8000/recipe/<recipe_id >/delete/ - Recipe delete page
· http://localhost:8000/profile/create/ - Profile create page
· http://localhost:8000/profile/details/ - Profile details page
· http://localhost:8000/profile/edit/ - Profile edit page
· http://localhost:8000/profile/delete/ - Profile delete page
1.2.Navigation bar-The "Catalogue", "Create Recipe", and "Profile" links on the navigation bar are only visible when the user has a profile;
1.3. Buttons

button "Create Profile"- Upon clicking on it, if the profile is successfully created, you should be redirected to the Catalogue page.
Otherwise, the form should display the relevant validation errors.
-A button "Create Recipe"-Upon clicking on it, if the recipe is successfully created, you should be redirected to the Catalogue page.
Otherwise, the form should display the relevant validation errors.
-A button "Details"("Catalogue Page") leading to the Recipe Details page for the selected recipe.

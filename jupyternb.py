{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0ff66dbc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6300b783",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies = pd.read_csv('tmdb_5000_movies.csv')\n",
    "credits = pd.read_csv('tmdb_5000_credits.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c6d5948a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>budget</th>\n",
       "      <th>genres</th>\n",
       "      <th>homepage</th>\n",
       "      <th>id</th>\n",
       "      <th>keywords</th>\n",
       "      <th>original_language</th>\n",
       "      <th>original_title</th>\n",
       "      <th>overview</th>\n",
       "      <th>popularity</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>production_countries</th>\n",
       "      <th>release_date</th>\n",
       "      <th>revenue</th>\n",
       "      <th>runtime</th>\n",
       "      <th>spoken_languages</th>\n",
       "      <th>status</th>\n",
       "      <th>tagline</th>\n",
       "      <th>title</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>vote_count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>237000000</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
       "      <td>http://www.avatarmovie.com/</td>\n",
       "      <td>19995</td>\n",
       "      <td>[{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...</td>\n",
       "      <td>en</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>In the 22nd century, a paraplegic Marine is di...</td>\n",
       "      <td>150.437577</td>\n",
       "      <td>[{\"name\": \"Ingenious Film Partners\", \"id\": 289...</td>\n",
       "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
       "      <td>2009-12-10</td>\n",
       "      <td>2787965087</td>\n",
       "      <td>162.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}, {\"iso...</td>\n",
       "      <td>Released</td>\n",
       "      <td>Enter the World of Pandora.</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>7.2</td>\n",
       "      <td>11800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      budget                                             genres  \\\n",
       "0  237000000  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...   \n",
       "\n",
       "                      homepage     id  \\\n",
       "0  http://www.avatarmovie.com/  19995   \n",
       "\n",
       "                                            keywords original_language  \\\n",
       "0  [{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...                en   \n",
       "\n",
       "  original_title                                           overview  \\\n",
       "0         Avatar  In the 22nd century, a paraplegic Marine is di...   \n",
       "\n",
       "   popularity                               production_companies  \\\n",
       "0  150.437577  [{\"name\": \"Ingenious Film Partners\", \"id\": 289...   \n",
       "\n",
       "                                production_countries release_date     revenue  \\\n",
       "0  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   2009-12-10  2787965087   \n",
       "\n",
       "   runtime                                   spoken_languages    status  \\\n",
       "0    162.0  [{\"iso_639_1\": \"en\", \"name\": \"English\"}, {\"iso...  Released   \n",
       "\n",
       "                       tagline   title  vote_average  vote_count  \n",
       "0  Enter the World of Pandora.  Avatar           7.2       11800  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "db246c28",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movie_id</th>\n",
       "      <th>title</th>\n",
       "      <th>cast</th>\n",
       "      <th>crew</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19995</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>[{\"cast_id\": 242, \"character\": \"Jake Sully\", \"...</td>\n",
       "      <td>[{\"credit_id\": \"52fe48009251416c750aca23\", \"de...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   movie_id   title                                               cast  \\\n",
       "0     19995  Avatar  [{\"cast_id\": 242, \"character\": \"Jake Sully\", \"...   \n",
       "\n",
       "                                                crew  \n",
       "0  [{\"credit_id\": \"52fe48009251416c750aca23\", \"de...  "
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "credits.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "9ac9a066",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'Series' object has no attribute 'merge'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_8908/183217141.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mmovies\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmovies\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmerge\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcredits\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mon\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'title'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\abcd\\lib\\site-packages\\pandas\\core\\generic.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m   5485\u001b[0m         ):\n\u001b[0;32m   5486\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 5487\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mobject\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__getattribute__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   5488\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   5489\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__setattr__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m->\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'Series' object has no attribute 'merge'"
     ]
    }
   ],
   "source": [
    "movies = movies.merge(credits,on='title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58229b29",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

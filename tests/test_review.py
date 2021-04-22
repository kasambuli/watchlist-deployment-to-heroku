import unittest
from app.models import Review,User
from app import db
from flask_login import current_user


class TestReview(unittest.TestCase):

  def setUp(self):
    self.user_burens = User(username = 'burens',password = 'banana',email='burensdev@gmail.com')
    self.new_review = Review(movie_id=12345, movie_title='Review',
                            image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='awesome movie',user=self.user_burens)

  def tearDown(self):
    Review.query.delete()
    User.query.delete()

  def test_check_instance_variables(self):
    self.assertEquals(self.new_review.movie_id,12345)
    self.assertEquals(self.new_review.movie_title,Review')
    self.assertEquals(self.new_review.image_path,
                      "https://image.tmdb.org/t/p/w500/jdjdjdjn")
    self.assertEquals(self.new_review.movie_review,'awesome movie')
    self.assertEquals(self.new_review.user,self.user_burens)

  def test_save_review(self):
      self.new_review.save_review()
      self.assertTrue(len(Review.query.all()) > 0)


  def test_get_review_by_id(self):

      self.new_review.save_review()
      got_reviews = Review.get_reviews(12345)
      self.assertTrue(len(got_reviews) == 1)
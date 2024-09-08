from django.test import TestCase
from tabom.models import Article, User
from tabom.services.like_service import do_like


class TestLikeService(TestCase):

    def test_simple(self) -> None:
        assert True

    def test_a_user_con_like_on_article(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test article")
        # When
        like = do_like(user.id, article.id)

        # Then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article.id)

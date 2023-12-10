from src.models import db, Post2, Comment, CommentVote, PostVote

class PostRepository:

    def get_post_by_id(self, post_id):
        post = Post2.query.filter_by(post_id=post_id).first()
        return post
      
    def get_posts_by_ids(self, post_ids):
        posts = Post2.query.filter(Post2.post_id.in_(post_ids)).all()
        return posts
    
    def create_post(self, title, content, community_name, timestamp, author_id):
        new_post = Post2(title, content, community_name, timestamp, author_id)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    def edit_post(self, existing_post, title, content, community_name) -> None:
        existing_post.title = title
        existing_post.content = content
        existing_post.community_name = community_name
        db.session.commit()

    def delete_post(self, post_to_delete):
        comments_to_delete = Comment.query.filter_by(post_id=post_to_delete.post_id).all()
        for comment in comments_to_delete:
            votes = CommentVote.query.filter_by(comment_id=comment.comment_id)
            for vote in votes:
                db.session.delete(vote)
                db.session.commit()
            db.session.delete(comment)
            db.session.commit()  
        votes = PostVote.query.filter_by(post_id=post_to_delete.post_id)
        for vote in votes:
            db.session.delete(vote)
            db.session.commit()        
        db.session.delete(post_to_delete)
        db.session.commit()        

    def get_all_posts_by_author_id(self, user_id):
        posts = Post2.query.filter_by(author_id=user_id).all()
        return posts
    
    def get_all_posts_by_post_votes(self, post_votes):
        posts = Post2.query.filter


    def get_all_posts(self):
        return Post2.query.all()
    
    
    
    # def create_post(self, author_id, title, content, community_name):
    #     #db.session.query(db.func.count(Vote.vote_id)).filter(Vote.post_id == self.post_id, Vote.is_upvote == True).scalar() - \ db.session.query(db.func.count(Vote.vote_id)).filter(Vote.post_id == self.post_id, Vote.is_upvote == False).scalar()
    #     new_post = Post2(author_id=author_id, title=title, content=content, community_name=community_name)
    #     db.session.add(new_post)
    #     db.session.commit()
    #     return new_post
    
    # def get_post_by_id(self, post_id):
    #     return Post2.query.get(post_id)
    
# Singleton to be used in other modules
post_repository_singleton = PostRepository()
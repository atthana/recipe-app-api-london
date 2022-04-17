from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from .serializers import TagSerializer


class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)  # อันนี้เรา comment ไปก็ได้นะ ถ้าเราไม่อยากใช้ ModHeader ในการจัดการกับ token
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):  # อันนี้ไม่เคยใช้เลย ต่างจาก create() ยังไงหว่า ที่เห็นชัดๆเลยคือ อันนี้มันรับเป็น serializer เข้ามา แทนที่จะเป็น request นะ
        """Create a new tag"""
        serializer.save(user=self.request.user)

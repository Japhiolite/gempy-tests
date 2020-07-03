def interpolate_zvals_at_xy(self, xy):
    assert xy[:, 0][0] <= xy[:, 0][-1], 'At the moment, the xy values of the first point must be smaller than second' \
                                        '(fix soon)'
    assert xy[:, 1][0] <= xy[:, 1][-1], 'At the moment, the xy values of the first point must be smaller than second' \
                                        '(fix soon)'
    xj = self.values_3D[:, :, 0][0, :]
    yj = self.values_3D[:, :, 1][:, 0]
    zj = self.values_3D[:, :, 2].T
    f = interpolate.RectBivariateSpline(xj, yj, zj)
    zi = f(xy[:, 0], xy[:, 1])
    return np.flipud(zi).diagonal()  # np.diag(zi)


def interpolate_zvals_at_xy_nw_se(self, xy):
    # assert xy[:, 0][0] <= xy[:, 0][-1], 'At the moment, the xy values of the first point must be smaller than second' \
    #                                    '(fix soon)'
    # assert xy[:, 1][0] <= xy[:, 1][-1], 'At the moment, the xy values of the first point must be smaller than second' \
    #                                    '(fix soon)'
    xj = self.values_3D[:, :, 0][0, :]
    yj = self.values_3D[:, :, 1][:, 0]
    zj = self.values_3D[:, :, 2]
    f = interpolate.interp2d(xj, yj, zj, kind='cubic')
    zi = f(xy[:, 0], xy[:, 1])
    if xy[:, 0][0] <= xy[:, 0][-1] and xy[:, 1][0] <= xy[:, 1][-1]:
        return np.diag(zi)
    else:
        return np.flipud(zi).diagonal()


    def _slice_topo_4_sections(self, p1, p2, resx, method='interp2'):
        xy = self.model.grid.sections.calculate_line_coordinates_2points(p1, p2, resx)
        if method=='interp2':
            z = self.model.grid.topography.interpolate_zvals_at_xy_nw_se(xy)
        else:
            z = self.model.grid.topography.interpolate_zvals_at_xy(xy)
        return xy[:, 0], xy[:, 1], z